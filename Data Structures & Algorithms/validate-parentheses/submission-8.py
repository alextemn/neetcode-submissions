class Solution:
    def isValid(self, s: str) -> bool:
        chars_map = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            print(stack)
            if c in '({[':
                stack.append(c)
            elif c in ')}]' and stack:
                if stack[-1] == chars_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
