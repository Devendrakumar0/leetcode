class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): 
            return s

        cols = len(s) 
        arr = [[""] * cols for _ in range(numRows)]

        row, col = 0, 0  
        down = True  

        for char in s:
            arr[row][col] = char  
            
            
            if row == numRows - 1:
                down = False  
            elif row == 0:
                down = True  
            
            if down:
                row += 1  
            else:
                row -= 1 
                col += 1  

        result = ""
        for r in arr:
            result += "".join(r)  
        
        return result
