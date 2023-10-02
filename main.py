import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")
            await websocket.send(f"Received your message: {message}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")

start_server = websockets.serve(handle_client, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

