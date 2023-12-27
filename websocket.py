from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

rooms = {}


@app.websocket("/ws/{room_id}/{player_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, player_id: int):
    await websocket.accept()
    if room_id not in rooms:
        rooms[room_id] = {"players": {player_id: websocket}}
    else:
        rooms[room_id]["players"][player_id] = websocket

    while True:
        data = await websocket.receive_text()
        # Process player's moves and update game state
        await notify_players(room_id, data)


async def notify_players(room_id: int, message: str):
    if room_id in rooms:
        for player_id, ws in rooms[room_id]["players"].items():
            await ws.send_text(message)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)