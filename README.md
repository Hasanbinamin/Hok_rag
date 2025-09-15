# Honor of Kings AI Strategy Coach

This project provides an AI-powered strategy coach for the game Honor of Kings. It leverages Google's Gemini-2.5-flash model and LangChain to process game-related documents and provide detailed strategic advice based on user queries.

## Features

*   **Document Loading:** Supports loading strategy guides and game data from `.txt` and `.pdf` files.
*   **Text Splitting:** Efficiently splits documents into manageable chunks for processing.
*   **Vector Database:** Utilizes Chroma DB to store and retrieve document embeddings, enabling semantic search for relevant information.
*   **Generative AI:** Integrates with Google's Gemini-2.5-flash model to generate comprehensive answers to strategic questions.
*   **RAG (Retrieval Augmented Generation):** Combines information retrieval with generative AI to provide context-aware responses, including hero overviews, counters, tips, rotation strategies, and practice recommendations.

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

### 4. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Google API Key

Obtain a Google API Key from the Google AI Studio ([https://aistudio.google.com/](https://aistudio.google.com/)) and set it as an environment variable. You can also directly embed it in `core.py` (as currently done), but using an environment variable is recommended for security.

```bash
export GOOGLE_API_KEY="YOUR_API_KEY"
```

### 6. Prepare Game Data

Place your game strategy documents (e.g., `DocHok.txt`, `HOK_C1.txt`, etc.) in the project root directory. The `core.py` file is configured to load these files.

### 7. Run the Application

Execute the `core.py` script to create the vector database and run a sample query:

```bash
python core.py
```

This will output a strategic response to the predefined query.

## Usage

You can modify the `query` variable in `core.py` to ask different strategic questions. You can also integrate the `get_rag_response` function into a larger application (e.g., a web interface using `app.py`).
