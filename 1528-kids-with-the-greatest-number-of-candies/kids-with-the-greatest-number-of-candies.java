class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> result = new ArrayList<Boolean>();
        int maxCandies = Integer.MIN_VALUE;
        for (int i = 0; i < candies.length; i++) {
            maxCandies = Math.max(maxCandies, candies[i]);
        }

        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= maxCandies) {
                result.add(true);
            } else {
                result.add(false);
            }
        }
        return result;
    }
}