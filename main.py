import os

from dotenv import load_dotenv
from fastapi import FastAPI

from src.presentation.controller import loan_router

load_dotenv()

app = FastAPI(title="Loan Eligibility API", version="1.0.0")

app.include_router(loan_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=os.getenv("HOST"), port=os.getenv("PORT"))
