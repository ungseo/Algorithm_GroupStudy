words = ['aya', 'ye', 'woo', 'ma']
babywords = ['aya', 'ye', 'woo', 'ma']

path = ['','','','']
visited = [0,0,0,0]
def FIND2WORDS(level, limit):
    if level == limit: 
        word = ''.join(path)
        babywords.append(word)
        return
    
    for i in range(4):
        if visited[i] == 1: continue
        path[level] = words[i]
        visited[i] = 1
        FIND2WORDS(level + 1, limit)
        visited[i] = 0

def solution(babbling):
    answer = 0
    FIND2WORDS(0,2)
    FIND2WORDS(0,3)
    FIND2WORDS(0,4)
    
    
    for i in babbling:
        if i in babywords:
            answer += 1
    return answer