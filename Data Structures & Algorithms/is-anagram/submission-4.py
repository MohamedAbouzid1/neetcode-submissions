class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        i = 0
        while i < len(s):
            if len(s) != len(t):
                return False
                break
            elif s[i] != t[i]:
                return False
            i += 1

        return True