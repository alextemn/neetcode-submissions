class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op != '+' and op != 'C' and op != 'D':
                records.append(int(op))
            if op == "+":
                records.append(records[-1] + records[-2])
            if op == "D":
                records.append(2 * records[-1])
            if op == "C":
                records.pop()
        return sum(records)