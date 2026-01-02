from dotenv import load_dotenv

from llm import HelloAgentsLLM
from ReActAgent import ReActAgent
from tools import ToolExecutor, get_current_time, search

# 加载 .env 文件中的环境变量
load_dotenv()

if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    tool_executor = ToolExecutor()
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    time_description = "获取当前日期和时间。当你需要知道现在是什么时候时应使用此工具。"
    tool_executor.registerTool("Search", search_description, search)
    tool_executor.registerTool("GetCurrentTime", time_description, get_current_time)
    ReActAgent(
        llm_client=llm_client,
        tool_executor=tool_executor,
    ).run("小米手机的最新型号是什么")
