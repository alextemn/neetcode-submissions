class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqList = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)

        for n in freq:
            freqList[freq[n]].append(n)
        
        for i in range(len(freqList)-1, 0, -1):
            if len(res) == k:
                break;
            if not freqList[i]:
                continue
            
            for n in freqList[i]:
                if len(res) < k:
                    res.append(n)
        return res