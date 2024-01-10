
def solution(n, wires):
    global cnt
    def dfs(y):
        global cnt

        for i in range(1, n+1):
            if i == y: continue
            if bit[i] == 1: continue
            if tree[y][i] == 0: continue
            bit[i] = 1
            cnt += 1
            dfs(i)

    answer = 999
    
    tree = [[0] * (n+1) for _ in range(n+1)]
    
    for i in wires:
        tree[i[0]][i[1]] = 1
        tree[i[1]][i[0]] = 1
    
    for i in wires:
        bit = [0] * (1+n)
        
        v1, v2 = i[0], i[1]
        tree[v1][v2] = 0
        tree[v2][v1] = 0
        cnt = 1
        bit[v1] = 1
        dfs(v1)
        tree[v1][v2] = 1
        tree[v2][v1] = 1
        
        a1 = n - cnt
        a2 = n - a1
        
        aa1 = min(a1,a2)
        aa2 = max(a1,a2)
        
        aa = aa2 - aa1
        print(aa)
        if aa <= answer:
            answer = aa
        

    return answer