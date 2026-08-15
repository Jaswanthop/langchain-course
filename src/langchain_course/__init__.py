from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI # pyright: ignore[reportMissingImports]
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


load_dotenv()



# def searchquery(query:str) -> str:
#     """
#     Tool that searches over the internet
#     Args:
#         query (str): The search query to be executed.
#     Returns:
#         str: The search results as a string.
#     """
#     print(f"Searching for: {query}")
#     return tavily_client.search(query)


#gemini llm
llm =ChatGoogleGenerativeAI(model="gemini-3.6-flash")
tools=[TavilySearch()]
agent = create_agent(model=llm, tools=tools)
def main() -> None:
    print("Hello from langchain!")
    result=agent.invoke({
        "messages": [HumanMessage(content="are there any openings for backend intern or java intern in india?")],
    })
    print(result)

if __name__ == "__main__":
    main()
