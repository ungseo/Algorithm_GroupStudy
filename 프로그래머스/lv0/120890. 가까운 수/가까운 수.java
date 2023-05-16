
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int minA = 10000;
        for (int i=0; i < array.length; i++) {
            int rst = Math.abs(array[i] - n);
            if (rst < minA) {
                minA = rst;
                answer = array[i];
            } else if (rst == minA ){
                if (answer > array[i]) {
                    answer = array[i];
                }
            }
        }
        return answer;
    }
}