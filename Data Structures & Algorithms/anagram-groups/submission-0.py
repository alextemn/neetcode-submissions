class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for s in st:
                count[ord(s)-ord('a')] += 1
            res[tuple(count)].append(st)

        res_list = list(res.values())
        return res_list