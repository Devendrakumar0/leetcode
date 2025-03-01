class Solution {
    public int[] applyOperations(int[] nums) {
        int j = 0;
        for(int i=1; i<nums.length; i++){
            if(nums.length == 2 && nums[i]!=nums[j] && nums[i]!=0 && nums[j]!=0) return nums;
            if(nums[i] == nums[j] && nums[i]!=0 && nums[j]!=0){
                nums[j] = nums[j]*2;
                nums[i] = 0;
                j++;
            }
            else{
                j++;
            }
        }
        int k = 0;
        for(int i = 0; i<nums.length; i++){
            if(nums[i]==0){
                k = i;
                break;
            }
        }
        for(int i = k+1; i<nums.length; i++){
            if(nums[i]!=0){
                reverse(nums, i, k);
                k++;
            }
        }
        return nums;
    }
    public void reverse(int[] nums, int i, int j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
}