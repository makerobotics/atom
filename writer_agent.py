from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv
import os

load_dotenv(override=True)
MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")
HOW_MANY_SEARCHES = int(os.getenv("HOW_MANY_SEARCHES", 10))

INSTRUCTIONS = f"""
You are a senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query, and some research.
Generate a comprehensive report based on the research and the query.
Start with a table of content listing the findings and containing the date, the scientists name and a brief description, then write a detailed report for each of the findings.
Explain each theory and experiment in detail, including the methodology, results, and implications.
Link all the research together as they are supposed to be related in time: 
Explain in each section how each research is linked to the previous and next in chronological order.

The final output should be in markdown format, and it should be lengthy and detailed. 
Keep the content in chronological order.
Aim for {HOW_MANY_SEARCHES//2} pages of content.
No need for introduction or conclusion, just the report.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    # Not used yet, but could be used to generate follow up questions for the user to research further
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(name="Writer Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=ReportData)
