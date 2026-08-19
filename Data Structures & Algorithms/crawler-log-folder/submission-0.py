class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for op in logs:
            if op[0] != '.':
                stack.append('d')
            if op == "../" and stack:
                stack.pop()
        return len(stack)