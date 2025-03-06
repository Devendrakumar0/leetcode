class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int N = n * n;
        int[] result = new int[2];
        boolean[] seen = new boolean[N + 1];
        for (int[] row : grid) {
            for (int num : row) {
                if (seen[num]) {
                    result[0] = num;
                }
                seen[num] = true;
            }
        }
        for (int i = 1; i <= N; i++) {
            if (!seen[i]) {
                result[1] = i;
                break;
            }
        }
        return result;
    }
}
