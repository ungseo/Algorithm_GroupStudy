class Solution {
    public int solution(int n) {
        int answer = 0;
        int d;
        while (n != 0) {
            d = n % 10;
            answer += d;
            n = n / 10;
        }
        return answer;
    }
}