class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        n = len(nums)
        for i in range(n):
            secondNum = target - nums[i]
            if secondNum in s:
                return [s[secondNum], i]
            s[nums[i]] = i
        return []