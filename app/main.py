from fastapi import FastAPI
import logging
from app.routers import parse

# 配置日志记录
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'  # 追加模式
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(parse.router)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the FastAPI project!"}
