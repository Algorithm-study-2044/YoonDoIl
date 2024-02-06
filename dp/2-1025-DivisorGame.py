class Solution:
    def divisorGame(self, n: int) -> bool:

        def get_divisors(k):
            res = []
            for i in range(1,k):
                if k%i == 0:
                    res.append(i)
            return res


        mem = [False, False, True, False]

        for i in range(4, n+1):
            divisors = get_divisors(i)
            win = False
            for divisor in divisors:
                if not mem[i-divisor]:
                    win = True
                    break
            mem.append(win)
                
        return mem[n]
