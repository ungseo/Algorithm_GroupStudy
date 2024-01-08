from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque()
    cur_weight = weight
    cur_length = 0
    while trucks:
        time += 1
        if cur_length == bridge_length: # 다리가 꽉찼으면
            cur_weight += bridge.popleft() # 다리 마지막 차 빼주고
            cur_length -= 1 # 다리 한칸씩 옮기기
        if cur_weight - trucks[0] >= 0:
            cur_weight -= trucks[0]
            bridge.append(trucks.popleft())
            cur_length += 1
        else:
            bridge.append(0)
            cur_length += 1
    return time + bridge_length
   