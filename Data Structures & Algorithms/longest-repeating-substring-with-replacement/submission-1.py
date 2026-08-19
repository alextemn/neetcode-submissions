class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        char_counter = {}
        st, e = 0, 0

        while e < len(s):
            char_counter[s[e]] = char_counter.get(s[e], 0) + 1
            if (max(char_counter.values()) + k) >= (e-st+1):
                max_len = max(max_len, e-st+1)
                e += 1
            else:
                char_counter[s[st]] -= 1
                st += 1
                char_counter[s[e]] -= 1
        return max_len