class MyQueue:

    def __init__(self):
        self.inputS = []
        self.outputS = []

    def push(self, x: int) -> None:
        self.inputS.append(x)

    def pop(self) -> int:
        if not self.outputS:
            while(self.inputS):
                self.outputS.append(self.inputS.pop())
        return self.outputS.pop()

    def peek(self) -> int:
        if not self.outputS:
            while(self.inputS):
                self.outputS.append(self.inputS.pop())
        return self.outputS[-1]

    def empty(self) -> bool:
        if not self.outputS and not self.inputS:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()