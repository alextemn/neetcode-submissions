class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bigDict = defaultdict(list)

        for i in range(len(strs)):
            bigDict[tuple(sorted(strs[i]))].append(strs[i])
        
        return list(bigDict.values())