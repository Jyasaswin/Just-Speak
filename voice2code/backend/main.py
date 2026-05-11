from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Command(BaseModel):
    text: str

@app.post("/process")
def process_command(command: Command):
    return {
        "received": command.text
    }
