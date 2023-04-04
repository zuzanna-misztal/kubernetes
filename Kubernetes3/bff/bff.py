from fastapi import FastAPI
import uvicorn
import urllib.request

app = FastAPI()

@app.get("/")
def root():
    return urllib.request.urlopen("http://api1-service/api1").read()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)