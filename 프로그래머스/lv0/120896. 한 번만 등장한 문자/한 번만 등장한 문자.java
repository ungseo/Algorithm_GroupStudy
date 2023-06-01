import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        char[] cArray = s.toCharArray();
        
        for (int i=0; i < cArray.length; i++) {
            char c = cArray[i];
            int cnt = 0;
            for (int j=0; j < cArray.length; j++) {
                if (cArray[j] == c) {
                    cnt ++;
                }
            }
            if (cnt == 1) {
                answer += c;
            }
        }
        char[] ans = answer.toCharArray();
        Arrays.sort(ans);
        
        return new String(ans);
    }
}