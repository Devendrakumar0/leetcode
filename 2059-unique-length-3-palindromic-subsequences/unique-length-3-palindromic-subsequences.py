class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()
        for ch in set(s):
            left = s.find(ch)
            right = s.rfind(ch)
            if right - left > 1:
                for middle in set(s[left + 1:right]):
                    unique_palindromes.add(ch + middle + ch)

        return len(unique_palindromes)
