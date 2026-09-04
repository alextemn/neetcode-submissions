class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def backtrack(cur, OPEN, CLOSE):
            if OPEN == CLOSE == n:
                res.add(cur)
                return
            
            if OPEN < n:
                cur += '('
                backtrack(cur, OPEN + 1, CLOSE)
                cur = cur[:-1]
            if CLOSE < OPEN:
                cur += ')'
                backtrack(cur, OPEN, CLOSE + 1)
                cur = cur[:-1]
            
            return
        backtrack("", 0, 0)
        return list(res)