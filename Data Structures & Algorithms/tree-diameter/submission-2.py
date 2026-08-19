class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        max_length = 0
        adj = {}
        for u,v in edges:
            if u in adj:
                adj[u].append(v)
            else:
                adj[u] = [v]
            if v in adj:
                adj[v].append(u)
            else:
                adj[v] = [u]
        
        def traversal(node, length, visited):
            nonlocal max_length
            max_length = max(max_length, length)
            visited.add(node)
            for n in adj[node]:
                if n not in visited:
                    traversal(n, length+1, visited)
            visited.remove(node)
            return
        
        for key in adj:
            traversal(key,0,set())
        
        return max_length