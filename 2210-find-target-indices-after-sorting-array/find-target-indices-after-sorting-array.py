class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        r=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                r.append(i)
        return r
                

        