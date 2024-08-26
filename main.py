import os
import pprint
import json
import time
from common import *  # 确保common.py文件中有evalEndTime函数的定义
from dotenv import load_dotenv  # type: ignore
from langchain_openai import ChatOpenAI

def main():
    try:
        start_time = time.time()  # 获取开始时间
        load_dotenv()  # 读取.env文件
        
        # 确保模型名称和初始化参数是正确的
        model = ChatOpenAI(model="gpt-3.5-turbo")

        # 调用模型获取建议
        result = model.invoke("我想去澳洲留学，给我一些建议好吗？")
        
        # 打印结果
        pprint.pprint(result.content)
        print()

        # 打印执行时间
        print(evalEndTime(start_time))

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()