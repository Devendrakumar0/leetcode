class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        r = []
        r.append(first)
        for i in range(1, len(encoded)+1):
            r.append(r[i-1] ^ encoded[i-1])
        return r

        