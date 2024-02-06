class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s) % 2 == 1:
            l, r = (len(s)//2), (len(s)//2)
        else:
            l = len(s)//2 - 1
            r = l + 1
        res_list = [""]*len(s)
        while r < len(s) and l >= 0:
            if s[l] != s[r]:
                if s[l] < s[r]:
                    res_list[l] = s[l]
                    res_list[r] = s[l]
                else:
                    res_list[l] = s[r]
                    res_list[r] = s[r]
            else:
                res_list[l] = s[r]
                res_list[r] = s[r]
            l -= 1
            r += 1
        return ''.join(res_list)


