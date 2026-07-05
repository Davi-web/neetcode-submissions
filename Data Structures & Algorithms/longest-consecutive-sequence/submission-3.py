class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        ss= set()
        for n in nums:
            ss.add(n)
        c = 1
        res = 1
        for s in sorted(ss):
            cur = s
            if cur - 1 in ss:
                print(cur)
                c += 1
                print(s , c)
            else:
                print(s , c)
                
                c =  1
            res = max(res, c)
            

        return res