from fastapi import FastAPI
from question import router as questionapi
from staticdata.question import router as static
from users.login import router as loginapi
from wordle.wordle import router as wordleapis
from mcq.mcq import router as mcqapis


app = FastAPI()

app.include_router(questionapi)
app.include_router(mcqapis)
app.include_router(wordleapis)
app.include_router(static)
app.include_router(loginapi)

from fastapi.responses import FileResponse

@app.get("/")
async def health_check():

    return FileResponse("home.html")
# If this script is executed, run the FastAPI application directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)