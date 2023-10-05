import asyncio
import websockets
import queue
from cash import get_pq_empty , get_pq
import threading
import time
# Create an empty priority queue
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
async def handle_client(websocket, path):
    try:
        # response = await websocket.recv()
        while True:
            # for x in array:
            #     await websocket.send(x)
            if not pq.empty():
                score = pq.get()
                print(score)
                await websocket.send(str(score))
            #     time.sleep(20)
            #     # response = await websocket.recv()
            #     # print(response)
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")

print("server")
start_server = websockets.serve(handle_client, "ec2-13-235-51-177.ap-south-1.compute.amazonaws.com", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()