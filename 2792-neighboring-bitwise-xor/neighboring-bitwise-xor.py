class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        from functools import reduce
        from operator import xor
        return reduce(xor, derived) == 0
        