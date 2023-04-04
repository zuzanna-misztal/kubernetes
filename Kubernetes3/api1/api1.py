from fastapi import FastAPI
import uvicorn
import urllib.request
from urllib.error import HTTPError

app = FastAPI()

@app.get("/api1")
def root():
    while True:
        try:    
            result = urllib.request.urlopen("http://api2-service/api2").read()
        except HTTPError as e:
            if e.code != 500:
                print("err code ", e.code)  
                print("err msg ", e.msg)                    
                break
        else:
            break
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)