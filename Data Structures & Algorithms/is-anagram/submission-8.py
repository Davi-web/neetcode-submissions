class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. sort both strings and check if they are equal. O(nlog(n))
        # O(nlog(n) + xmlog(m)) Time complexity for sorting both string, 
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True