#!/usr/bin/env python

import asyncio
from websockets.server import serve
import datetime
import os
from typing import NoReturn, TextIO

PORT = os.getenv("PY_WEBSOCKET_PORT_NUMBER", 8765)


async def echo(websocket: any) -> NoReturn:
    with open("messages.txt", "w") as f:
        async for message in websocket:
            formatted_text = f"received: {message} at {datetime.datetime.utcnow().isoformat()+'Z'}"
            f.write(formatted_text + "\n")
            print(formatted_text)
            await asyncio.sleep(1)
            await send_message(f, websocket, message)


async def send_message(f: TextIO, websocket, message: str) -> NoReturn:
    await websocket.send(message)
    ts_string = datetime.datetime.utcnow().isoformat()+'Z'
    formatted_text = f"sent: {message} at {ts_string}"
    f.write(formatted_text + "\n")
    print(formatted_text)


async def main() -> NoReturn:
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    print(f"Starting server at {PORT}")
    asyncio.run(main())
