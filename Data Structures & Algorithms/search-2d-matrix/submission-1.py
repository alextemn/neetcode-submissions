class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_length = len(matrix[0])
        row_length = len(matrix)
        row = 0
        col = col_length - 1
        
        while row < row_length and col >= 0:
            current = matrix[row][col]
            print(current)
            if current < target:
                row += 1
            elif current > target:
                col -= 1
            else:
                return True 
        return False