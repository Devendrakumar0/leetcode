class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                matrix[row][col] += min(matrix[row - 1][max(0, col - 1):col + 2])
        return min(matrix[-1])


      
# The class Solution contains a method minFallingPathSum which takes a matrix of integers as input and returns the minimum falling path sum.
# The function starts by determining the number of rows n in the input matrix.
# It then iterates through each row of the matrix starting from the second row (index 1). In each iteration, it goes through each element in the row.
# For each element in the current row, the code calculates the minimum falling path sum by considering the three possible paths from the above row. The value at the current position is updated to include the minimum of these three paths.
# The function returns the minimum value in the last row of the updated matrix, representing the minimum falling path sum across the entire matrix.
# The code uses Python's list slicing to get the range of values from the above row for the three possible paths.
# Overall, the code uses dynamic programming to iteratively calculate and update the minimum falling path sum for each position in the matrix, and it returns the minimum sum found in the last row.
