from bootstrap.application import create_app
from config.config import settings
import uvicorn

app = create_app()

@app.get("/health")
async def root():
    return "health"