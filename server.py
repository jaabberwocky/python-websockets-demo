#!/usr/bin/env python

import asyncio
from websockets.server import serve
from websockets.exceptions import ConnectionClosedOK
import datetime
import os
from typing import NoReturn, TextIO
import json

PORT = os.getenv("PY_WEBSOCKET_PORT_NUMBER", 8765)
CONNECTED = set()


async def handler(websocket: any) -> NoReturn:
    CONNECTED.add(websocket)
    with open("messages.txt", "w") as f:
        try:
            async for event in websocket:
                event_dict = json.loads(event)
                await log_incoming_message(f, websocket, event_dict)

                if event_dict['type'] == 'message':
                    for connected_websocket in CONNECTED:
                        await send_message(f, connected_websocket, event_dict['message'])
                elif event_dict['type'] == 'ping':
                    await send_ping(f, websocket)
                else:
                    await send_error(f, websocket, "invalid message type")
        except:
            print("error: closing connection.")


async def send_ping(f: TextIO, websocket) -> NoReturn:
    ts_string = datetime.datetime.utcnow().isoformat()+'Z'
    await websocket.send(json.dumps({
        'type': 'pong',
        'ts': ts_string
    }))
    formatted_text = f"sent: pong at {ts_string}"
    f.write(formatted_text + "\n")
    print(formatted_text)


async def log_incoming_message(f: TextIO, websocket, event_dict: dict) -> NoReturn:
    ts_string = datetime.datetime.utcnow().isoformat()+'Z'
    formatted_text = f"received: {event_dict} at {ts_string}"
    f.write(formatted_text + "\n")
    print(formatted_text)


async def send_error(f: TextIO, websocket, message: str) -> NoReturn:
    ts_string = datetime.datetime.utcnow().isoformat()+'Z'
    await websocket.send(json.dumps({
        'type': 'error',
        'message': message,
        'ts': ts_string
    }))
    formatted_text = f"sent: {message} at {ts_string}"
    f.write(formatted_text + "\n")
    print(formatted_text)


async def send_message(f: TextIO, websocket, message: str) -> NoReturn:
    ts_string = datetime.datetime.utcnow().isoformat()+'Z'
    await websocket.send(json.dumps({
        'type': 'message',
        'message': message,
        'ts': ts_string
    }))
    formatted_text = f"sent: {message} at {ts_string}"
    f.write(formatted_text + "\n")
    print(formatted_text)


async def main() -> NoReturn:
    async with serve(handler, "localhost", 8765):
        try:
            await asyncio.Future()  # run forever
        except ConnectionClosedOK:
            print("Connection closed")

if __name__ == "__main__":
    print(f"Starting server at {PORT}")
    asyncio.run(main())
