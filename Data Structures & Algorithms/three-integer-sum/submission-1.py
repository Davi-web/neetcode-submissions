class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j !=k and k != i and nums[i] + nums[j] + nums[k] ==0 and i < j < k:
                        res.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(i) for i in res]