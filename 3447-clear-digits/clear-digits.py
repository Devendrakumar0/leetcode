class Solution:
    def clearDigits(self, s: str) -> str:
        result = ""  
        i = 0  
        while i < len(s):
            if s[i].isdigit():
                result = result[:-1]  
            else:
                result += s[i] 
            i += 1 
        return result
        