import java.util.HashMap;

class Solution {
    public long solution(String numbers) {
        String answer = "";
        HashMap<String,String> dic = new HashMap<>();
        dic.put("zero", "0");
        dic.put("one", "1");
        dic.put("two", "2");
        dic.put("three", "3");
        dic.put("four", "4");
        dic.put("five", "5");
        dic.put("six", "6");
        dic.put("seven", "7");
        dic.put("eight", "8");
        dic.put("nine", "9");
        
        StringBuilder ck = new StringBuilder();
        for (char s : numbers.toCharArray()) {
            ck.append(s);
            if (dic.containsKey(ck.toString())) {
                answer += dic.get(ck.toString());
                ck.setLength(0);
            }
        }
        
        return Long.parseLong(answer.toString());
    }
}