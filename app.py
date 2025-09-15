from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from core import get_rag_response
app = FastAPI()

@app.get("/chat")
def hello(user_input: str = Query(..., description="The user question")):
    result = get_rag_response(user_input)
    return {"message": result}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)