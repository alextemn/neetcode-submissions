class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stacky = []
        stacky.append(s[0])
        index = 1

        if len(s) == 1:
            return False

        while index < len(s):
            if s[index] in '([{':
                stacky.append(s[index])

            elif s[index] == ')':
                if not stacky or stacky[-1] != '(':
                    return False
                stacky.pop()

            elif s[index] == ']':
                if not stacky or stacky[-1] != '[':
                    return False
                stacky.pop()

            elif s[index] == '}':
                if not stacky or stacky[-1] != '{':
                    return False
                stacky.pop()

            index += 1

        return len(stacky) == 0