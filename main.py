import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            await websocket.send(f"Received your message:hi")
            message = await websocket.recv()
            print(f"Received message: {message}")
            user_input = input("Enter Reply: ")
            await websocket.send(f"Received your message: {user_input}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")
print("server")
start_server = websockets.serve(handle_client, "ec2-13-235-51-177.ap-south-1.compute.amazonaws.com", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

