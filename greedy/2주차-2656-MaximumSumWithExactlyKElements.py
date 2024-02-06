class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s = 0
        m = max(nums)
        for _ in range(k):
            s += m
            m += 1
        return s
