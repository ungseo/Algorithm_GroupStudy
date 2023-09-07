class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int len = str2.length();
        int st = 0;
        int ed = st + len;
        while (ed != str1.length()+1) {
            if (str1.substring(st,ed).equals(str2)) {
                
                answer = 1;
            }
            st++;
            ed++;
        }
        if (answer == 1) {
            answer = 1;
        } else {
            answer = 2;
        }
        return answer;
    }
}