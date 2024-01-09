def solution(numbers, target):
    branch = len(numbers)
    used = [0] * branch
    answer = 0

    def dfs(level):
        nonlocal answer
        if level == branch:
            sum = 0
            for i in range(branch):
                if used[i] == 1:
                    sum += numbers[i]
                else:
                    sum -= numbers[i]
            if sum == target:
                answer += 1
            return
        for i in range(2):
            used[level] = i
            dfs(level + 1)
    dfs(0)
    return answer