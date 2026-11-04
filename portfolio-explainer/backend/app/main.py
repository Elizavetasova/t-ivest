from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import portfolio, explain


app = FastAPI(
    title="Portfolio Explainer API",
    version="0.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    portfolio.router,
    prefix="/api/v1"
)

app.include_router(
    explain.router,
    prefix="/api/v1"
)


@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}