from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv(override=True)

client = AsyncOpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)
model = OpenAIChatCompletionsModel(
    model=os.getenv("LLM_MODEL"),
    openai_client=client,
)

INSTRUCTIONS = """
You are a research assistant. Given a search term, you search for that term and 
produce a concise summary of the results. The summary must be 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
Explain why it matters, how it builds on previous research and how it will lead to future experiments.
"""

class SearchData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    hypothesis: str = Field(description="Reason why the experiment was made and what it was trying to prove")

search_agent = Agent(name="Search Agent", instructions=INSTRUCTIONS, model=model)