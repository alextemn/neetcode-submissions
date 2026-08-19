class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words)+1)
        res = []
        for i in range(1, len(words) + 1):
            if (words[i-1][0] == 'a' or words[i-1][0] == 'e' or words[i-1][0] == 'i' or words[i-1][0] == 'o' or words[i-1][0] == 'u') and (words[i-1][-1] == 'a' or words[i-1][-1] == 'e' or words[i-1][-1] == 'i' or words[i-1][-1] == 'o' or words[i-1][-1] == 'u'):
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
        
        for li, ri in queries:
            res.append(prefix[ri+1] - prefix[li])
        return res