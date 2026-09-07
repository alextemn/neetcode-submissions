class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        time = -1
        noFruit = True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    noFruit = False
        if not queue and noFruit:
            return 0
        
        while queue:
            qLen = len(queue)

            for _ in range(qLen):
                r, c = queue.popleft()
                grid[r][c] = 2
                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    queue.append([r-1,c])
                if r+1 < len(grid) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    queue.append([r+1,c])
                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    queue.append([r,c-1])
                if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    queue.append([r,c+1])
            time += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return time       