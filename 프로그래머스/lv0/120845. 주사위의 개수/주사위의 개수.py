def solution(box, n):
    f = box[0] // n
    s = box[1] // n
    t = box[2] // n
    answer = f * s * t
    return answer