'''nonblocking code, asynchronous programming provides opportunities 
for a program to continue running 
other code while waiting for a long-running task to complete'''
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(3)  # NON-BLOCKING
    print("Data fetched")

async def main():
    print("Start")
    task = asyncio.create_task(fetch_data())
    print("Doing other work...")
    await task
    print("End")

asyncio.run(main())
