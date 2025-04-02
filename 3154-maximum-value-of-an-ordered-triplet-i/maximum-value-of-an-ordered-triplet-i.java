class Solution {
    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        if (n < 3) return 0;

        int maxPrefix = nums[0];
        int maxDiff = Integer.MIN_VALUE;
        long maxTripletValue = 0;

        for (int j = 1; j < n - 1; j++) {
            maxDiff = Math.max(maxDiff, maxPrefix - nums[j]);
            maxTripletValue = Math.max(maxTripletValue, (long) maxDiff * nums[j + 1]);
            maxPrefix = Math.max(maxPrefix, nums[j]);
        }
        
        return maxTripletValue;
    }
}
