from fastapi import FastAPI, HTTPException
import uvicorn
from random import randint

app = FastAPI()

@app.get("/api2")
def root():
    rand = randint(0, 1)
    if rand:
        return "Hello from Api2"
    else:
        raise HTTPException(status_code=500, detail="Something went wrong")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)