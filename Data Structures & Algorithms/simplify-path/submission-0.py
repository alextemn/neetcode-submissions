class Solution:
    def simplifyPath(self, path: str) -> str:
        # gonna use a stack here, but shold ask more about what happens if we go to a previous dir, but there is none (guessing nothing happens since you can't pop an empty stack)
        stack = collections.deque()
        string = ""

        start, end = 0, 0

        while end < len(path):
            while end < len(path) and path[start] == '/' and path[end] == '/':
                start += 1
                end += 1

            while end < len(path) and path[end] != '/':
                end += 1

            if path[start:end] == '..':
                if stack:
                    stack.pop()
            elif path[start:end] != '.' and path[start:end] != "":
                stack.append(path[start:end])

            while start < len(path) and path[start] != '/' and end != len(path):
                start += 1
            
        if not stack:
            return '/'
            
        for _ in range(len(stack)):
            item = stack.popleft()
            string += '/'
            string += item
        
        return string