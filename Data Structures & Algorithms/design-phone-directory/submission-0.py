class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.numbers = [False] * maxNumbers
        self.nextNumber = 0
        self.releasedNumbers = []
        self.maxNumbers = maxNumbers

    def get(self) -> int:
        if self.nextNumber == self.maxNumbers and not self.releasedNumbers:
            return -1
        elif self.nextNumber == self.maxNumbers:
            used = self.releasedNumbers.pop()
            self.numbers[used] = True
            return used
        else:
            self.numbers[self.nextNumber] = True
            self.nextNumber += 1
            return self.nextNumber-1

    def check(self, number: int) -> bool:
        if self.numbers[number] == False:
            return True
        return False

    def release(self, number: int) -> None:
        self.numbers[number] = False
        self.releasedNumbers.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
