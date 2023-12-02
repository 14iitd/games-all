from fastapi import FastAPI

from mcq.question import router as postapi
from users.login import router as loginapi

app = FastAPI()

app.include_router(postapi)
app.include_router(loginapi)


@app.get("/")
async def health_check():

    return {"Message": "To access APIs put /docs in the URL."}
# If this script is executed, run the FastAPI application directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)