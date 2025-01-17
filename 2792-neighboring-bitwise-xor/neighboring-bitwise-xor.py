class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        derived_sum = 0
        for num in derived:
            derived_sum ^= num
        return derived_sum == 0
        