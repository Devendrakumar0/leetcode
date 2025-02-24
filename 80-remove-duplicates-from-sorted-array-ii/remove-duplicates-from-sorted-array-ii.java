class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for(int j = 2; j<nums.length; j++){
            if(nums[j]!=nums[i]){
                nums[i+2] = nums[j];
                i += 1;
            }
        }
        return i+2;
    }
}