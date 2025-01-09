class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n=len(words)
        result = []
        i=0
        for i in range(n):
            x=words[i]
            for j in range(n):
                if (x in words[j]) and (x not in result) and (x!=words[j]):
                    result.append(x)
        return result
            
        