import time
from fastapi import Request

from app.helper.logger import logger


async def http_logger(request: Request, call_next):
    # before
    start_time = time.time()
    response = await call_next(request)
    # after
    process_time = time.time() - start_time
    # request.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Request: {round(process_time, 3)}秒 {response.status_code} {request.method} {request.url}")
    return response