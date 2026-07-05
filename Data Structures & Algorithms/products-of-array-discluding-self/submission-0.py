class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        pre[0] = nums[0]
        post[n - 1] = nums[n - 1]
        for i in range(1, n):
            pre[i] = nums[i] * pre[i - 1]
        for j in range(n - 2, -1, -1):
            post[j] = nums[j] * post[j + 1]
        res = [0] * n
        res[0] = post[1]
        res[n - 1] = pre[n - 2]
        for i in range(1, n - 1):
            res[i] = pre[i - 1] * post[i + 1]
        return res
            