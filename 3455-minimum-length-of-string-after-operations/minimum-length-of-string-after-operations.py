class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        result = 0
        for i in freq.values():
            if i % 2 == 0:
                result += 2
            else:
                result += 1
        return result


        