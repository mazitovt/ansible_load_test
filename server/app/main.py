import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/result/")
async def get_known_people():
    result = 1
    return {"result": f"{result}"}

@app.get("/")
async def get_known_people():
    result = 1
    return {"result": f"{result}"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
