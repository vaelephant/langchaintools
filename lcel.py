import time
from common import *  # 确保common.py文件中有evalEndTime函数的定义
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # 使用OpenAI API
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


def main():
    try:
        # 获取开始时间
        start_time = time.time()

        # 读取.env文件
        load_dotenv()

        # 使用格式化字符串定义消息模板
        template = """
        系统: 你是一位{career}专家，你经常辅导你的学生。
        用户: 我想学习{language}，给我几个建议好吗？
        """

        # 创建聊天提示模板
        prompt_template = ChatPromptTemplate.from_template(template)

        # 初始化大语言模型
        model = ChatOpenAI(

            # 指定模型的名称，这里使用的是 "gpt-3.5-turbo"
            model_name="gpt-3.5-turbo",
            # 设置生成文本的最大 tokens 数量为 100
            max_tokens=100,
            # 设置 top_p 参数为 1.0，表示使用 nucleus sampling
            top_p=1.0,
            # 设置 temperature 参数为 0.9，控制生成文本的随机性
            temperature=0.9,
            # 设置 frequency_penalty 参数为 0.0，控制生成文本中重复词的惩罚
            frequency_penalty=0.0,

        )

        # 使用Chain调用模型
        chain = prompt_template | model | StrOutputParser()

        # 调用模型获取建议
        result = chain.invoke({"career": "医生", "language": "按摩"})
        print(result)

        # 打印执行时间
        print(evalEndTime(start_time))

    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    main()
