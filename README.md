# Honor of Kings AI Strategy Coach

This project provides an AI-powered strategy coach for the game Honor of Kings. It leverages Google's Gemini-2.5-flash model and LangChain to process game-related documents and provide detailed strategic advice based on user queries.

## Features

*   **Document Loading:** Supports loading strategy guides and game data from `.txt` and `.pdf` files.
*   **Text Splitting:** Efficiently splits documents into manageable chunks for processing.
*   **Vector Database:** Utilizes Chroma DB to store and retrieve document embeddings, enabling semantic search for relevant information.
*   **Generative AI:** Integrates with Google's Gemini-2.5-flash model to generate comprehensive answers to strategic questions.
*   **RAG (Retrieval Augmented Generation):** Combines information retrieval with generative AI to provide context-aware responses, including hero overviews, counters, tips, rotation strategies, and practice recommendations.

## Project Structure

*   `app.py`: FastAPI application that exposes an endpoint for chatting with the AI coach.
*   `core.py`: Contains the core logic for document loading, text splitting, vector database creation, and RAG chain. It can also be run as a standalone script for testing.
*   `requirements.txt`: Lists all Python dependencies required for the project.
*   `data/`: Directory to store your game strategy documents (`.txt` and `.pdf` files).
*   `chroma_store/`: Directory where the Chroma vector database is persisted.
*   `font-end/`: Contains the `index.html` file for a simple frontend interface .
*   `.env`: File to store environment variables like your Google API Key (You need to make on by you self like : GOOGLE_API_KEY= *********).

## Setup Instructions

### 1. Clone the Repository (if not already done)

```bash
git clone <your-repository-url>
cd tast_project
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

*   **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```
After activating, it's good practice to upgrade pip:
```bash
python -m pip install --upgrade pip
```

### 4. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Google API Key

Obtain a Google API Key from the Google AI Studio (https://aistudio.google.com/) and set it as an environment variable.

It is recommended to create a `.env` file in the project root and add your API key there:

```
GOOGLE_API_KEY="YOUR_API_KEY"
```
The `core.py` script is configured to load this key using `python-dotenv`.

### 6. Prepare Game Data

Place your game strategy documents (e.g., `DocHok.txt`, `HOK_C1.txt`, etc.) in the `data/` directory. The `core.py` file is configured to load these files.

## Running the Application

There are two ways to run the application:

### 1. As a FastAPI Backend

The `app.py` file provides a FastAPI backend with a chat endpoint.

To run the FastAPI application:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
This will start the API server, typically accessible at `http://127.0.0.1:8000/docs` for the OpenAPI documentation.

### 2. As a Standalone Script (for testing)

The `core.py` script can be executed directly to test the RAG functionality with a predefined query.

```bash
python core.py
```

This will output a strategic response to the predefined query in the terminal.

## Usage

You can modify the `query` variable in `core.py` to ask different strategic questions. You can also integrate the `get_rag_response` function into a larger application, such as the provided `app.py` FastAPI interface or a custom frontend application.

If you are using the FastAPI backend (`app.py`), you can interact with it via its `/chat` endpoint. For example, using `curl` or a web browser:

```bash
curl "http://127.0.0.1:8000/chat?user_input=What%20is%20the%20best%20way%20to%20play%20Marksman%20heroes%3F"
```
Or, you can use index.html file in font-end folder (e.g., `font-end/index.html`) it can make requests to this endpoint.
