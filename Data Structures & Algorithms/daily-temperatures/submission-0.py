class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        temp_stack = []
        temp_stack.append([0,temperatures[0]])
        for i in range(1, len(temperatures)):
            while temp_stack and temperatures[i] > temp_stack[-1][1]:
                out[temp_stack[-1][0]] = i - temp_stack[-1][0]
                temp_stack.pop()
            temp_stack.append([i, temperatures[i]])
        
        return out