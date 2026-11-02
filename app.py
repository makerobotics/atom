import asyncio
import os

from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

HOW_MANY_SEARCHES = int(os.getenv("HOW_MANY_SEARCHES", 10))

query = f"Which are the {HOW_MANY_SEARCHES} most important experiences and theories done by scientists to understand the atom. How do they build on each other? Start from Democritus"

# This is a coroutine and not a function, so we need to run it in an event loop (asyncio.run(main()))
async def main():
    # Consumes the ResearchManager.run() generator and prints the status updates and final report
    async for status_update in ResearchManager().run(query):
        # This print statement is printing the yielded status updates and final report from the ResearchManager.run() generator.
        print(status_update, flush=True)


if __name__ == "__main__":
    # As main is now a coroutine, we need to run it in an event loop (asyncio.run(main()))
    asyncio.run(main())