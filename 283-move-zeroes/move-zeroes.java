class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int j = -1;
        for(int i = 0; i<n; i++){
            if(nums[i]==0) {
                j = i;
                break;
            }
        }
        if(j==-1) return;
        for(int i = j+1; i<n; i++){
            if(nums[i]!=0){
                reverse(nums, i, j);
                j++;
            }
        }
    }
        private void reverse(int[] nums, int start, int end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
        }
    }
    
