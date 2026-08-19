class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs, visited):
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre, visited):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True
        for i in range(len(adj)):
            if not dfs(i, set()):
                return False
        return True