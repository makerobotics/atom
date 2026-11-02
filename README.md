# Atom Research Assistant

An asynchronous, model-powered research pipeline that plans research topics, generates summaries, writes a chronological Markdown report, and saves it to `report.md`.

The current query focuses on the history of atomic theory and experiments, beginning with Democritus.

## How it works

1. The planner proposes research topics based on the query.
2. The search agent generates a concise summary for each topic. Planned summaries run concurrently.
3. The writer combines the summaries into a detailed report in chronological order.
4. The report agent formats and saves the report as `report.md`.
5. The application prints progress updates and the final report to the terminal.

> **Note:** The search agent does not currently have a web-search tool configured. It asks the model to summarize each topic, but this code does not itself retrieve or verify external sources.

## Requirements

- Python 3.12 or newer
- An OpenAI API key
- [uv](https://docs.astral.sh/uv/) for dependency management

## Setup

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_api_key