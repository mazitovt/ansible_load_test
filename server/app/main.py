import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/result/")
async def get_known_people():
    result = count_prime_numbers(100)
    return {"result": f"{result}"}

@app.get("/")
async def get_known_people():
    result = count_prime_numbers(100)
    return {"result": f"{result}"}

def count_prime_numbers(n):
    c = 0
    for num in range(2, n + 1):
        i = 1
        for i in range(2, num):
            if(num % i == 0):
                i = num
                break
        # If the number is prime then print it.
        if(i != num):
            c += 1
    
    return c

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
