class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique_nums = {}
        self.nums = collections.deque(nums)

        for n in nums:
            self.unique_nums[n] = self.unique_nums.get(n, 0) + 1

    def showFirstUnique(self) -> int:
        while self.nums and self.unique_nums[self.nums[0]] > 1:
            self.nums.popleft()
        
        if self.nums:
            return self.nums[0]
        else:
            return -1

    def add(self, value: int) -> None:
        self.unique_nums[value] = self.unique_nums.get(value, 0) + 1
        self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
