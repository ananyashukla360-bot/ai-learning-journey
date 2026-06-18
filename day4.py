import asyncio
import time

async def fetch_data(name, delay):
    print(f"Starting {name}...")
    await asyncio.sleep(delay)  # simulates a slow API call
    print(f"Finished {name}!")
    return f"{name} result"

async def main():
    start = time.time()
    
    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 2),
        fetch_data("API 3", 2),
    )
    
    end = time.time()
    print(results)
    print(f"Total time: {end - start:.2f} seconds")

asyncio.run(main())