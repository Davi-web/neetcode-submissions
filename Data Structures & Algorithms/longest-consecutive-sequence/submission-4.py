class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        ss= set()
        for n in nums:
            ss.add(n)
        c = 1
        res = 1
        for s in ss:
           if s - 1 not in ss:
            c = 1
            while (s + c) in ss:
                c += 1
            res = max(res, c)
            

        return res