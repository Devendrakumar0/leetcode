class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        double_nums = nums + nums
        n = len(nums)
        for i in range(n):
            if double_nums[i:i+n] == sorted_nums:
                return True
        return False