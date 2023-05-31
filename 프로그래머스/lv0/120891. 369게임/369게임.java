class Solution {
    int answer = 0;
    public int solution(int order) {
        String temp = Integer.toString(order);
        
        for (int i=0; i < temp.length(); i++) {
            if (temp.charAt(i) == '3' || temp.charAt(i) == '6' || temp.charAt(i) == '9') {
                answer += 1;
            }
        }
        
        return answer;
    }
}