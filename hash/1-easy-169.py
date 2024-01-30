from collections import defaultdict

class Solution:
    def mySolution(self, nums):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for k, v in d.items():
            if v > len(nums)//2:
                return k

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
            
        return candidate
