class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""  
        maxi = 0 
        for i in s:
            if i in temp:
                temp = temp[temp.index(i) + 1:] 
            temp += i 
            maxi = max(maxi, len(temp)) 
        return maxi
        
        
        