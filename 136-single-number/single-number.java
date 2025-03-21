class Solution {
    public int singleNumber(int[] nums) {
        int c = 0;
        int k = 0;
        for(int i:nums){
            int num = i;
            c=0;
            for(int j:nums){
                if(num==j) c+=1;
            }
            if(c==1) k=i;
        }
        return k;
    }
}