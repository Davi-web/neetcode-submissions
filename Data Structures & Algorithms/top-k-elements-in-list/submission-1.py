class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        a = []
        for num, cnt, in count.items():
            a.append([cnt, num])
        a.sort()
        res = []
        for i in range(k):
            res.append(a[len(a) - 1 - i][1])
        return res