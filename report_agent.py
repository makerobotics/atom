from agents import Agent, function_tool, ModelSettings
from LLM_Model import model

settings = ModelSettings(tool_choice="required")

@function_tool
def report_tool(subject: str, text_body: str) -> str:
    """
    Generate a markdown report with the given subject and body
    
    Args:
        subject: The subject of the report
        text_body: The body of the report as markdown
    """
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(f"{text_body}\n")
    return "Report generated successfully"


INSTRUCTIONS = """
You are provided with a detailed report. Use your tool to create a markdown report, converting the report into
a clean, well presented markdown file with an appropriate subject line.
"""

report_agent = Agent(name="Report Agent", instructions=INSTRUCTIONS, tools=[report_tool], model=model, model_settings=settings)