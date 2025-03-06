class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int newLength = (int)Math.pow(grid.length, 2);
        int[] res = new int[newLength];
        int[] result = new int[2];
        int k = 0;
        for(int i = 0;i<grid.length;i++){
            for(int j = 0; j<grid[i].length;j++){
                if(check(res, grid[i][j])==false){
                    result[0] = grid[i][j];
                }
                else{
                    res[k++] = grid[i][j];
                }
            }
        }
        TreeSet<Integer> Uniq = new TreeSet<>();
        for(int i:res){
            Uniq.add(i);
        }
        
        Integer[] arr = Uniq.toArray(new Integer[0]);
        for(int i: arr){
            System.out.print(i + " ");
        }
        for(int i=0; i<res.length;i++){
            if((i+1)!=arr[i]){
                result[1] = arr[i]+1;
            }
        }
        return result;
    }
    public boolean check(int[] res, int key){
            for(int i:res){
                if(i==key) return false;
            }
            return true;
        }
}