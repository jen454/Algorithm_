import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        Arrays.sort(array);
        int answer = 0;
        int com = 99;
        for (int i=0; i<array.length; i++) {
            if (Math.abs(array[i]-n) == com) continue;
            else if (Math.abs(array[i]-n) < com) {
                com = Math.abs(array[i]-n);
                answer = array[i];
            }
        }
        return answer;
    }
}