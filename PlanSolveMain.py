from dotenv import load_dotenv

from llm import HelloAgentsLLM
from PlanSolve import PlanAndSolveAgent

# 加载 .env 文件中的环境变量
load_dotenv()

if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    plan_slove = PlanAndSolveAgent(llm_client)
    plan_slove.run(
        "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    )
    print(f"总消耗 Token 数: {llm_client.total_tokens}")
