class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result=[]
        vowels=['a', 'e', 'i', 'o', 'u']
        n = len(words)
    
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
           
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]
        
        for start, end in queries:
            result.append(prefix_sum[end + 1] - prefix_sum[start])
        return result
            

        