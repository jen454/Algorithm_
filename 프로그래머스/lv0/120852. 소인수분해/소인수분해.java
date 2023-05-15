import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        int[] ans = {};
        List<Integer> list = new ArrayList<>();
        for (int i=2; i<=n; i++) {
            if (n%i==0) {
                while(n%i==0) {
                    n /= i;
                }
                list.add(i);
            }
        }
        ans = list.stream().distinct().mapToInt(Integer::intValue).toArray();
        return ans;
    }
}