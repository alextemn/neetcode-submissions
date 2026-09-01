class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        out = []
        p, a = set(), set()

        def dfs(r, c, visited, prev):
            if heights[r][c] < prev:
                return
            visited.add((r, c))

            if r + 1 < rows and (r + 1, c) not in visited and heights[r+1][c] >= prev:
                dfs(r+1, c, visited, heights[r][c])
            if r - 1 >= 0 and (r - 1, c) not in visited and heights[r-1][c] >= prev:
                dfs(r-1, c, visited, heights[r][c])
            if c + 1 < cols and (r, c + 1) not in visited and heights[r][c+1] >= prev:
                dfs(r, c+1, visited, heights[r][c])
            if c - 1 >= 0 and (r, c - 1) not in visited and heights[r][c-1] >= prev:
                dfs(r, c-1, visited, heights[r][c])
            return
        
        for c in range(cols):
            dfs(0, c, p, heights[0][c])
            dfs(rows - 1, c, a, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, p, heights[r][0])
            dfs(r, cols - 1, a, heights[r][cols-1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in a and (r,c) in p:
                    out.append([r,c])
        return out