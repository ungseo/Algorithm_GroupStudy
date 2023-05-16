import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        Arrays.sort(sides);
        int a,b,c;
        a = sides[0];
        b = sides[1];
        c = sides[2];
        if (a+b>c) {
            answer = 1;
        } else {
            answer = 2;
        }
    
            
        return answer;
    }
}