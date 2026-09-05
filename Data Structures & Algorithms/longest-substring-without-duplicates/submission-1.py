class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        chars = {}
        
        while r < len(s):
            while s[r] in chars and chars[s[r]] > 0:
                chars[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            if not s[r] in chars or chars[s[r]] == 0:
                chars[s[r]] = chars.get(s[r], 0) + 1
                r += 1
            
        return longest
