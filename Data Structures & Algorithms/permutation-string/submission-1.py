class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}
        s, e = 0, len(s1)-1
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
        while e < len(s2):
            print(s2_dict)
            if s2_dict == s1_dict:
                return True
            else:
                s2_dict[s2[s]] -= 1
                if s2_dict[s2[s]] == 0:
                    del s2_dict[s2[s]]
                s += 1
                e += 1
                if e < len(s2):
                    s2_dict[s2[e]] = s2_dict.get(s2[e], 0) + 1
        return False