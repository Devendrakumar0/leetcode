class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        total_sum = sum(nums)

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        c = 0
        for i in range(n - 1): 
            left_sum = prefix_sum[i]
            right_sum = total_sum - prefix_sum[i]
            if left_sum >= right_sum:
                c += 1

        return c

        