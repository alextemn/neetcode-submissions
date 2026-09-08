class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        maxPath = 0
        cache = [([-1] * cols) for _ in range(rows)]
        
        def dfs(r, c, prevVal):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prevVal:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]

            res = 1
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))

            cache[r][c] = res

            return res
        
        for r in range(rows):
            for c in range(cols):
                maxPath = max(maxPath, dfs(r, c, -1))
        
        return maxPath