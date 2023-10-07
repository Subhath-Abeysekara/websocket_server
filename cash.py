import queue
import time

pq = queue.PriorityQueue()
x = []
def set_pq(score):
    global x
    time_ = time.time()
    # pq.put((time_, score))
    x.append(score)
    return

def get_pq_empty():
    global x
    return True if x == [] else False

def get_pq():
    global x
    return x