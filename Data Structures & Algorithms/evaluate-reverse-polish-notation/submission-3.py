class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        start = 0
        end = len(tokens) - 1
        stack = []

        while start <= end:
            print(stack)
            if tokens[start] not in '+-*/':
                stack.append(int(tokens[start]))
                start += 1
            else:
                if tokens[start] == "+":
                    tmp = int(stack[-1]) + int(stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                    start += 1
                elif tokens[start] == "-":
                    tmp = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                    start += 1
                elif tokens[start] == "*":
                    tmp = int(stack[-1]) * int(stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                    start += 1
                elif tokens[start] == "/":
                    tmp = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(int(tmp))
                    start += 1
        print(stack)
        return stack[0]
                