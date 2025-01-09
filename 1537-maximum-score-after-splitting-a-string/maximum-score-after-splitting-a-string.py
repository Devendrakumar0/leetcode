class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        maxi = 0
        for i in range(1, n):
            right = s[i:]
            left = s[:i]
            left_score = left.count("0")
            right_score = right.count("1")
            score = left_score + right_score
            if score>maxi:
                maxi = score
        return maxi


        