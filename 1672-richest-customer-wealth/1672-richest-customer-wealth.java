import java.util.Arrays;

class Solution {
    public int maximumWealth(int[][] accounts) {
        int[] answer = new int[accounts.length];
        for (int i=0; i<accounts.length; i++) {
            answer[i] = Arrays.stream(accounts[i]).sum();
        }
        return Arrays.stream(answer).max().getAsInt();
    }
}