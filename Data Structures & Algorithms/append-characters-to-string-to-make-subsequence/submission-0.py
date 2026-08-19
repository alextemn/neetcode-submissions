class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPtr, tPtr = 0, 0

        while sPtr < len(s):
            if tPtr >= len(t):
                return 0
            if s[sPtr] == t[tPtr]:
                tPtr += 1
            sPtr += 1
        return len(t) - tPtr