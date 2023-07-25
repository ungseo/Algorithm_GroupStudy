import sys
from queue import PriorityQueue
input = sys.stdin.readline


def deikstra():
    q = PriorityQueue()
    size = route[obj_st-1].qsize()
    for i in range(size):
        q.put(route[obj_st-1].get())

    while q:
        curPrice, curSt = q.get()
        if curSt + 1 == obj_ed:
            print(curPrice)
            return
        size = route[curSt].qsize()
        for i in range(size):
            pop = route[curSt].get()
            q.put((curPrice + pop[0], pop[1]))


# Input
N = int(input())
M = int(input())
route = [PriorityQueue() for _ in range(N)]
for i in range(M):
    st, ed, price = map(int, input().split())
    route[st - 1].put((price, ed - 1))

obj_st, obj_ed = map(int, input().split())


deikstra()
