class Solution {
    public int[] solution(int[] array) {
        int maxV = 0;
        int maxIdx = 0;
        
        for (int i=0; i<array.length; i++) {
            if (maxV < array[i]) {
                maxV = array[i];
                maxIdx = i;
            }
        }
        int[] answer = {maxV, maxIdx};
        
        return answer;
    }
}