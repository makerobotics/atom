import os
from pydantic import BaseModel, Field
from agents import Agent
from LLM_Model import model

HOW_MANY_SEARCHES = int(os.getenv("HOW_MANY_SEARCHES", 10))

INSTRUCTIONS = f"""
You are a research assistant. Given a user query, come up with a set of searches
to perform to best answer the query. Output {HOW_MANY_SEARCHES} terms to query for.
The most relevant and well known findings should be listed. Less relevant findings should be ignored.
"""

class SearchItem(BaseModel):
    # Keep this order !!
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the search.")


class SearchPlan(BaseModel):
    searches: list[SearchItem] = Field(description="A list of searches to perform to best answer the query.")
    
planner_agent = Agent(name="Planner Agent", instructions=INSTRUCTIONS, model=model, output_type=SearchPlan)
