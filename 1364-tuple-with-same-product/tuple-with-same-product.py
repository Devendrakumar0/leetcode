class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = {} 
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_map:
                    product_map[product] += 1
                else:
                    product_map[product] = 1

        for freq in product_map.values():
            if freq > 1:
                count += freq * (freq - 1) * 4  
        return count
        