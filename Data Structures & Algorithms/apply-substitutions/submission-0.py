class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        res = []
        rMap = {}
        for key, val in replacements:
            rMap[key] = val
        
        def dfs(key):
            i = 0
            while i < len(rMap[key]):
                if rMap[key][i] == "%":
                    rMap[key] = rMap[key][:i] + dfs(rMap[key][i+1]) + rMap[key][i+3:]
                i += 1
            return rMap[key]
        j = 0
        while j < len(text):
            for i in range(len(text[j:])):
                if text[j+i] == "%":
                    res.append(text[j:j+i])
                    j += i
                    break
            res.append(dfs(text[j+1]))
            j += 3
        return "".join(res)