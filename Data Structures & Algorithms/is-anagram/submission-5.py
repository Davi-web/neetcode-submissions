class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. sort both strings and check if they are equal. O(nlog(n))
        # O(2 * nlog(n)) Time complexity for sorting both string, 
        return sorted(s) == sorted(t)