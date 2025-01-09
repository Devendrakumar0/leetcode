class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        score=[]
        for i in range(1, n):
            score.append(s[i:].count("1") + s[:i].count("0"))
        return max(score)


        