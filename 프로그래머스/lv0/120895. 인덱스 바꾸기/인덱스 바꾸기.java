class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        
        for (int i=0; i<my_string.toCharArray().length; i++) {
            if (i == num1) {
                answer += my_string.toCharArray()[num2];
            } else if (i == num2) {
                answer += my_string.toCharArray()[num1];
            } else {
                answer += my_string.toCharArray()[i];
            }
        }
        
        return answer;
    }
}