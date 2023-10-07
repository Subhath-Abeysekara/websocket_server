import asyncio
import websockets
import queue
import time
import cash
pq = queue.PriorityQueue()

# Add elements to the priority queue with priorities
time_ = time.time()
pq.put((time_, {"task":"Task B"}))  # Task A arrived first
time.sleep(1)
time_ = time.time()
pq.put((time_, "Task A"))  # Task B arrived second
time.sleep(1)
time_ = time.time()
pq.put((time_, "Task C"))
array = ["a","b","c","d","e","f","g","h","i","j"]

async def handle_client_(websocket):
    await websocket.send("str(score)")

async def handle_client(websocket, path):
    try:
        while True:
            print(cash.get_pq_empty())
            if not cash.get_pq_empty():
                break
                # await websocket.send(str(cash.get_pq()))

    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")

print("server")
start_server = websockets.serve(handle_client, "ec2-13-235-16-145.ap-south-1.compute.amazonaws.com", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()