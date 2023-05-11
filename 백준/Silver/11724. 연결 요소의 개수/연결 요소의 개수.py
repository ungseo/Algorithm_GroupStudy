# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def bfs(st):
#     q = deque()
#     q.append(st)
#     path = [0] * (N + 1)
#     path[st] = 1
#     while q:
#         cur_node = q.popleft()
#
#         for i in arr[cur_node]:
#             if path[i] == 1: continue
#             path[i] = 1
#             q.append(i)
#
#     temp = []
#     for i in range(1, N + 1):
#         if path[i] == 1:
#             temp.append(i)
#     if temp in CC: return
#     CC.add(temp)
#     return
#
#
# CC = set()
# N, M = map(int, input().split())
# arr = [[] for _ in range(N + 1)]
# for i in range(M):
#     a, b = map(int, input().split())
#     arr[a].append(b)
#     arr[b].append(a)
#
# for i in range(1, N + 1):
#     bfs(i)
#
# print(len(CC))

import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
seqnum = [0] * (node+1)
seq = 1
ans = node

for _ in range(edge):

    valid = True
    a, b = map(int, input().split())
    if seqnum[a]==0 and seqnum[b]==0:
        seqnum[a] = seqnum[b] = seq
        seq += 1
    elif seqnum[a]==0:
        seqnum[a] = seqnum[b]
    elif seqnum[b]==0:
        seqnum[b] = seqnum[a]
    else:
        if seqnum[a]==seqnum[b]:
            valid = False
        else:
            low_s = min(seqnum[a], seqnum[b])
            high_s = max(seqnum[a], seqnum[b])
            for i in range(1, node+1):
                if seqnum[i]==high_s:
                    seqnum[i] = low_s
    # print(seqnum) ###
    if valid:
        ans -= 1

print(ans)