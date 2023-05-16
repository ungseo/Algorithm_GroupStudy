import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(int[] num_list, int n) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0 ; i < num_list.length; i+=n) {
            arr.add(num_list[i]);
        }
        return arr;
    }
}