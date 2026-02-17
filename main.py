from dotenv import load_dotenv 
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from tavily import TavilyClient
from langchain_tavily import TavilySearch


llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
tools = [TavilySearch()]
agent = create_agent(llm, tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for data scientist in new york on linkedin and list all their details")})
    print(result)

if __name__ == "__main__":
    main()
