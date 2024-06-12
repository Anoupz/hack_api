.PHONY: install run watch

# Install dependencies
install:
	poetry install

# Run the Flask app
run:
	poetry run flask run

# Watch mode to restart the server on changes
watch:
	poetry run flask run --reload