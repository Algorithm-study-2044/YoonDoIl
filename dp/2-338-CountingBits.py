class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [-1]*(n+1)
        if n == 0:
            return [0]
        ans[0] = 0
        ans[1] = 1
        p = 0
        for i in range(2, n+1):
            if i == 2**(p+1):
                ans[i] = 1
                p += 1
            else:
                ans[i] = ans[i-2**p] + 1

        return ans
