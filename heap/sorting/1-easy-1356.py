class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count1s(num):
            binRes = []
            curr = num
            while curr > 0:
                binRes.append(curr % 2)
                curr //= 2
            return sum(binRes)
        arrSorted = sorted(arr)
        arrSorted = sorted(arrSorted, key=lambda x: count1s(x))
        return arrSorted
