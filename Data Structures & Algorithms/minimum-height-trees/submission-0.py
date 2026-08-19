class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        heights = [[] for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node, visited):
            queue = collections.deque()
            queue.append(node)
            visited.add(node)
            h = -1
            while queue:
                for i in range(len(queue)):
                    cur = queue.popleft()
                    for j in range(len(adj[cur])):
                        if adj[cur][j] not in visited:
                            queue.append(adj[cur][j])
                            visited.add(adj[cur][j])
                h += 1
            return h
        minH = float('inf')
        for node in range(len(adj)):
            heights[node] = bfs(node, set())
            minH = min(minH, heights[node])
        for i in range(len(heights)):
            if heights[i] == minH:
                res.append(i)
        return(res)