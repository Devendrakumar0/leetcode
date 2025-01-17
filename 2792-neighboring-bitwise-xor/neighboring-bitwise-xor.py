class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        def is_valid(original_start):
            original = [0] * n
            original[0] = original_start
            for i in range(1, n):
                original[i] = derived[i - 1] ^ original[i - 1] 
            return (derived[-1] ^ original[-1]) == original[0]
        return is_valid(0) or is_valid(1)
        