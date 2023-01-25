import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/api2")
def root():
    return "Api 2"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)