class Solution {
    public int[] runningSum(int[] nums) {
        int[] answer = new int[nums.length];

        for (int i=1; i<nums.length+1; i++) {
            for (int j=0; j<i; j++) {
                answer[i-1] += nums[j];
            }
        }

        return answer;
    }
}

// 0 01 012 0123