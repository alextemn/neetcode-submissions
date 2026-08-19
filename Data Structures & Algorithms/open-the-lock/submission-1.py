class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque()
        queue.append("0000")
        turns = 0
        visited = set("0000")

        if "0000" in deadends:
            return -1
        while queue:
            qLen = len(queue)

            for i in range(qLen):
                cur = queue.popleft()
                if cur == target:
                    return turns

                for j in range(4):
                    new1 = cur[:j] + str((int(cur[j]) - 1) % 10) + cur[j+1:]
                    new2 = cur[:j] + str((int(cur[j]) + 1) % 10) + cur[j+1:]
                    if new1 not in deadends and new1 not in visited:
                        queue.append(new1)
                        visited.add(new1)
                    if new2 not in deadends and new2 not in visited:
                        queue.append(new2)
                        visited.add(new2)
            turns += 1

        return -1