import java.util.ArrayList;

class Solution {
    public ArrayList solution(int n) {
        ArrayList answer = new ArrayList();
        
        for (int i=1; i <= n; i++) {
            if (n % i == 0) {
                answer.add(i);
            }
        }
        
        return answer;
    }
}