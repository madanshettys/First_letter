from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the First Letter API!"}

@app.post("/process")
async def process_input(msg: Message):
    words = msg.text.strip().split()
    first_letters = [w[0] for w in words if w]
    return {"reply": f"First letters are: {' '.join(first_letters)}"}
