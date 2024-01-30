class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]

        from queue import PriorityQueue
        q = PriorityQueue(len(stones))
        for weight in stones:
            q.put(-1*weight)
        while q.qsize() > 1:
            x = q.get()
            y = q.get()
            if x != y:
                q.put(-1*abs(x-y))
        
        if q.empty():
            return 0
        else:
            return abs(q.get())


        
