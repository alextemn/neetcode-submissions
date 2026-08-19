class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        oneD = False
        sPtr, tPtr = 0, 0
        if abs(len(t)-len(s)) > 1 or s == t:
            return False
        while tPtr < len(t) and sPtr < len(s):

            if not oneD and s[sPtr] != t[tPtr] and len(s) == len(t):
                oneD = True
                tPtr += 1
                sPtr += 1
                continue
            elif not oneD and s[sPtr] != t[tPtr] and len(s) > len(t):
                oneD = True
                sPtr += 1
                continue
            elif not oneD and s[sPtr] != t[tPtr] and len(s) < len(t):
                oneD = True
                tPtr += 1
                continue
            elif s[sPtr] == t[tPtr]:
                sPtr += 1
                tPtr += 1
            else:
                return False
        return True