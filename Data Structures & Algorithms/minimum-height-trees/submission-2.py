class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        degree = [0] * n
        res = []

        for u,v in edges:
            adj[u].append(v)
            degree[u] += 1
            adj[v].append(u)
            degree[v] += 1
        
        queue = collections.deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        remain = n
        while remain > 2:
            q_len = len(queue)
            remain -= q_len
            for i in range(q_len):
                node = queue.popleft()
                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)
        return list(queue)