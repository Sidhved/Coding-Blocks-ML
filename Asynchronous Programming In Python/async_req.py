import asyncio
import aiohttp
import time

async def fetchFromWeb():
    url = "https://www.google.com"
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    async with open("file.txt", "w") as file:
        await resp.content.read(256)
    await session.close()

async def main():
    print(time.strftime('%X'))
    await asyncio.gather(
        *[fetchFromWeb() for _ in range(20)]
    )
    print(time.strftime('%X'))

if __name__ == "__main__":
    asyncio.run(main())