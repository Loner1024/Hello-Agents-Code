import os
from datetime import datetime
from typing import Callable, Dict, Protocol, TypedDict


class SearchClient(Protocol):
    def search(params: dict) -> dict: ...


class SerperSearchClient:
    def __init__(self):
        self.serper_api_key = os.getenv("SERPER_API_KEY")

    def search(self, params: dict) -> dict:
        import json

        import requests

        url = "https://google.serper.dev/search"

        payload = json.dumps(params)
        headers = {
            "X-API-KEY": self.serper_api_key,
            "Content-Type": "application/json",
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()


def search(query: str, search_client=SerperSearchClient) -> str:
    """
    一个基于SerperApi的实战网页搜索引擎工具。
    它会智能地解析搜索结果，优先返回直接答案或知识图谱信息。
    """
    print(f"🔍 正在执行网页搜索: {query}")

    params = {
        "q": query,
        "gl": "cn",  # 国家代码
        "hl": "zh-cn",  # 语言代码
        "autocorrect": True,
    }
    try:
        results = search_client().search(params)
        # 智能解析:优先寻找最直接的答案
        if "answerBoxList" in results:
            return "\n".join(results["answerBoxList"])
        if "answerBox" in results and "answer" in results["answerBox"]:
            return results["answerBox"]["answer"]
        if "knowledgeGraph" in results and "description" in results["knowledgeGraph"]:
            return results["knowledgeGraph"]["description"]
        if "organic" in results and results["organic"]:
            # 如果没有直接答案，则返回前三个有机结果的摘要
            snippets = [
                f"[{i + 1}] {res.get('title', '')}\n{res.get('snippet', '')}"
                for i, res in enumerate(results["organic"][:3])
            ]
            return "\n\n".join(snippets)

        return f"对不起，没有找到关于 '{query}' 的信息。"

    except Exception as e:
        return f"搜索时发生错误: {e}"


def get_current_time() -> str:
    """
    获取当前日期和时间的工具。

    Returns:
        str: 格式化的当前日期时间字符串
    """
    print("⏰ 正在获取当前时间")
    try:
        current_time = datetime.now()
        # 返回易读的日期时间格式
        return current_time.strftime("%Y年%m月%d日 %H:%M:%S %A")
    except Exception as e:
        return f"获取时间时发生错误: {e}"


class Tool(TypedDict):
    description: str
    func: Callable


class ToolExecutor:
    """
    一个工具执行器，负责管理和执行工具。
    """

    def __init__(self):
        self.tools: Dict[str, Tool] = {}

    def registerTool(self, name: str, description: str, func: Callable):
        """
        向工具箱中注册一个新工具。
        """
        if name in self.tools:
            print(f"警告:工具 '{name}' 已存在，将被覆盖。")
        self.tools[name]: Tool = {"description": description, "func": func}
        print(f"工具 '{name}' 已注册。")

    def getTool(self, name: str) -> Callable | None:
        """
        根据名称获取一个工具的执行函数。
        """
        return self.tools.get(name, {}).get("func")

    def getAvailableTools(self) -> str:
        """
        获取所有可用工具的格式化描述字符串。
        """
        return "\n".join(
            [f"- {name}: {info['description']}" for name, info in self.tools.items()]
        )
