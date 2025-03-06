class Solution {
    public boolean isFascinating(int n) {
        String str = "" + n + (n * 2) + (n * 3);
        if (str.length() != 9 || str.contains("0")) {
            return false;
        }
        boolean[] seen = new boolean[10];
        for (char c : str.toCharArray()) {
            int digit = c - '0';
            if (seen[digit]) {
                return false;
            }
            seen[digit] = true;
        }
        return true;
    }
}
