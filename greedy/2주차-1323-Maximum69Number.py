class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = []
        while num:
            digits.append(num%10)
            num //= 10
        res = 0
        flag = False
        for i in range(len(digits)-1, -1, -1):
            res *= 10
            if digits[i] == 6 and not flag:
                res += 9
                flag = True
            else:
                res += digits[i]
        return res
