function solution(num, k) {
    let answer = 0;
    num = num.toString();
    k = k.toString();
    if (num.includes(k)) {
        for (let i = 0; i < num.length; i++) {
            if (num[i] == k) {
                answer = ++i;
                break;
            }
        }
    } else {
        answer = -1;
    }
    return answer;
}