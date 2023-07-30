import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for i in operations:
        cmd, number = map(str, i.split())
        number = int(number)
        if cmd == 'I':
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            
        elif min_heap:
            if number == 1:
                a = heapq.heappop(max_heap)
                min_heap.remove(-a)
            else:
                a = heapq.heappop(min_heap)
                max_heap.remove(-a)
        
    if min_heap:
        answer.append(-heapq.heappop(max_heap))
        answer.append(heapq.heappop(min_heap))
    else:
        answer = [0, 0]
    return answer