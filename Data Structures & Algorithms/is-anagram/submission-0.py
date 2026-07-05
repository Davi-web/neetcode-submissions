class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for c in s:
            a[c] = a.get(c, 0) + 1
        for c in t:
            a[c] = a.get(c, 0) - 1
        print(a)
        for key, val in a.items():
            if val != 0:
                return False
        return True