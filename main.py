import time
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import asyncio
from cash import set_pq , get_pq_empty
import queue
import time
# Create an empty priority queue

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/")
def main():
    return "home"
@app.route("/v1/scoreupdate",methods=["POST"])
@cross_origin()
def scoreupdate():
    score = request.json['score']
    set_pq(score)
    print(get_pq_empty())
    return "success"
# async def handle_client(websocket, path):
#     try:
#         while True:
#             if not pq.empty():
#                 await websocket.send(pq.get())
#     except websockets.exceptions.ConnectionClosedOK:
#         print("Client disconnected")
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
    # print("server")
    # start_server = websockets.serve(handle_client, "localhost", 8765)
    #
    # asyncio.get_event_loop().run_until_complete(start_server)
    # asyncio.get_event_loop().run_forever()