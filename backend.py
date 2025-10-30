from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SafetyEvent(BaseModel):
    frame: int
    distance: float
    status: str

log = []  # store safety events

@app.post("/update")
def update_status(event: SafetyEvent):
    log.append(event.dict())
    print(f"[LOG] Frame {event.frame} -> {event.status}")
    return {"message": "Status updated"}

@app.get("/safety-status")
def get_status():
    return log
