# Search Agent

A minimal Python search agent built with LangChain that uses:

- OpenRouter for LLM inference
- Tavily for live web search
- Pydantic schemas for structured responses

It is currently configured to run a practical query for AI engineer job postings and print the agent result.

## What This Project Does

`search-agent` creates a tool-using LLM agent and asks it a search question. The agent:

1. Uses Tavily to fetch relevant web information.
2. Uses an OpenRouter-backed model to synthesize an answer.
3. Returns output shaped by a Pydantic schema (`AgentResponse` with `answer` and `sources`).

## Tech Stack

- Python 3.12+
- [LangChain](https://python.langchain.com/)
- [langchain-openrouter](https://pypi.org/project/langchain-openrouter/)
- [langchain-tavily](https://pypi.org/project/langchain-tavily/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Project Structure

```text
.
|- main.py
|- pyproject.toml
`- README.md
```

## Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd search-agent
```

### 2. Create environment and install dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or using `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 4. Run

```bash
python main.py
```

## Current Behavior

The script runs a predefined query in `main.py`:

```python
query = "search for 3 active job postings for an ai engineer using langchain in the Nagpur,India on linkedin and list their details?"
```

Then it prints the agent response object to stdout.

## Customize

### Change the query

Edit `query` inside `main()` in `main.py`.

### Change model

Update the model string in `main.py`:

```python
llm = ChatOpenRouter(model="nvidia/nemotron-3-super-120b-a12b-20230311:free", temperature=0)
```

### Change output schema

Modify these Pydantic models in `main.py`:

- `Source`
- `AgentResponse`

## Notes

- Make sure your API keys are valid and active.
- Tavily results can vary over time as the web changes.
- OpenRouter model availability can change; swap to another model if needed.

## Roadmap Ideas

- Add CLI arguments for query/model selection.
- Pretty-print structured output instead of raw dict/message dump.
- Add retries and graceful error handling for API failures.
- Add unit tests for response schema and query flow.