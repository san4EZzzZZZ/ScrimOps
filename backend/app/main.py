from fastapi import FastAPI

app = FastAPI(
    title="ScrimOps API",
    summary="Backend API for ScrimOps",
    discription="Управление киберспртивной платформой ScrimOps",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}