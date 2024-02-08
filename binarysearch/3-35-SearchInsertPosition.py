class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(l, r, t):
            while l+1<r:
                mid = (l+r)>>1
                if nums[mid] <= t:
                    l = mid
                else:
                    r = mid
            if nums[l] >= t:
                return l
            else:
                return l+1
        return search(0, len(nums), target)
