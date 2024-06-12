# Hackathon Project

A project to parse natural language text and generate filter formulas for contract searches using Crew AI and Groq.

## Setup

### Prerequisites

- Python 3.9+
- Virtual Environment (recommended)
- Poetry (for dependency management)

```bash
pip install poetry
```

### Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd hackathon
    ```

2. **Set up a virtual environment:**
    ```bash
    poetry shell
    ```

3. **Install dependencies:**
    ```bash
    make install
    ```

4. **Set up environment variables:**
    - Create an API key from [Groq Console](https://console.groq.com/keys).
    - Create an API key from [AgentOps Console](https://app.agentops.ai).
    - Create a `.env` file in the project root and add the following variables:
    ```env
    GROQ_API_KEY=your_groq_api_key
    AGENTOPS_API_KEY=your_agentops_api_key
    FLASK_APP=hackathon.main
    FLASK_ENV=development
    ```

## Usage

### Running the Application

To run the Flask application, use the following command:
```bash
make run