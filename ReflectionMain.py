from dotenv import load_dotenv

from llm import HelloAgentsLLM
from ReflectionAgent import ReflectionAgent

# 加载 .env 文件中的环境变量
load_dotenv()

if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    reflection_agent = ReflectionAgent(llm_client)
    reflection_agent.run("编写一个Python函数，输出前10个斐波那契数")
    print(f"总消耗 Token 数: {llm_client.total_tokens}")
