import logging

import agentops
from flask import Flask, request, jsonify
from flask_cors import CORS

from hackathon.crew import ParseTextCrew
from hackathon.config.config import setup_logging
from dotenv import load_dotenv


load_dotenv()
agentops.init()

# Setup logging
setup_logging()

# Initialize Flask app
app = Flask(__name__)
CORS(app)
logger = logging.getLogger("app")


@app.route("/")
def verify_app():
    logger.info("Received request at root endpoint")
    return jsonify({"message": "App is running!"})


@app.route("/api/parse_text", methods=["POST"])
def parse_text():
    filter_text = request.json.get("filter_text")
    logger.info(f"Received filter_text: {filter_text}")

    # Prepare the input for the crew task
    inputs = {"filter_text": filter_text}

    try:
        # Initialize the crew instance and execute the task
        crew_instance = ParseTextCrew()
        result = crew_instance.crew().kickoff(inputs=inputs)
        logger.info("Task executed successfully")
        return jsonify({"response": result})
    except Exception as e:
        logger.error(f"Error executing task: {e}", exc_info=True)
        return (
            jsonify({"error": "An error occurred while processing your request"}),
            500,
        )


if __name__ == "__main__":
    logger.info("Starting Flask app")
    app.run(debug=True)
