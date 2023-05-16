import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public ArrayList<Integer> solution(String my_string) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=0; i < my_string.length(); i++) {
        String s = my_string.substring(i,i+1);
        try {
            Integer a = Integer.parseInt(s);
            answer.add(a);
        } 
        catch (NumberFormatException ex) {
            
        }
        
        }
        Collections.sort(answer);
        return answer;
    }
}