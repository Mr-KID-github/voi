import re
from datetime import datetime
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def parse_input(sentence: str) -> dict:
    logger.info(f"Parsing sentence: {sentence}")
    
    # 使用当前日期
    date = datetime.now()
    logger.info(f"Current date: {date.strftime('%Y-%m-%d')}")

    # 解析金额
    amount_match = re.search(r'(\d+(\.\d+)?)元', sentence)
    amount = float(amount_match.group(1)) if amount_match else 0.0
    logger.info(f"Parsed amount: {amount}")

    # 解析类别
    categories = ["聚餐", "购物", "交通", "娱乐", "其他"]
    category = "其他"
    for cat in categories:
        if cat in sentence:
            category = cat
            break
    logger.info(f"Parsed category: {category}")

    # 生成备注
    remark = f"{category}花了{amount}元"
    logger.info(f"Generated remark: {remark}")

    # 生成结果字典
    result = {
        "日期": date.strftime('%Y-%m-%d'),
        "金额": amount,
        "类别": category,
        "备注": remark
    }

    logger.info(f"Result: {result}")
    return result
