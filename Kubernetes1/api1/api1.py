from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/api1")
def root():
    return "Api 1"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)