class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] lst = s.split(" ");
        for (int i=0; i < lst.length; i++) {
            try {
                Integer n = Integer.valueOf(lst[i]);
                answer += n;
            }
            catch (NumberFormatException ex) {
                answer -= Integer.parseInt(lst[i-1]);
            }
        }
        return answer;
    }
}