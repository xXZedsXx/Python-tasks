from fastapi import FastAPI
from apii import get_statistics

app = FastAPI()

@app.get("/stats")
async def stat(url: str):
    statistic = get_statistics(url)
    #return {"message":"Hello wordl"}
    return statistic