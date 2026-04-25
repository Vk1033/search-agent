from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage
from typing import List
from pydantic import BaseModel, Field

load_dotenv()

class Source(BaseModel):
    """Schema for a source of information."""
    url: str=Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent's response."""
    answer: str=Field(description="The answer to the user's query")
    sources: List[Source]=Field(default_factory=List,description="A list of sources used to generate the answer")

llm = ChatOpenRouter(model="nvidia/nemotron-3-super-120b-a12b-20230311:free", temperature=0)
tools = [TavilySearch()]
agent = create_agent(llm, tools, response_format=AgentResponse)

def main():
    query = "search for 3 active job postings for an ai engineer using langchain in the Nagpur,India on linkedin and list their details?"
    response = agent.invoke({"messages": HumanMessage(content=query)})
    print(response)


if __name__ == "__main__":
    main()
