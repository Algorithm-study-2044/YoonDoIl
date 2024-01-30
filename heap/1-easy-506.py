class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        from queue import PriorityQueue
        q = PriorityQueue(len(score)) 
        for i in range(len(score)):
            q.put((-1*score[i],i))
        res = [0]*len(score)
        for i in range(len(score)):
            currIdx = q.get()[1]
            if i == 0:
                res[currIdx] = "Gold Medal"
            elif i == 1:
                res[currIdx] = "Silver Medal"
            elif i == 2:
                res[currIdx] = "Bronze Medal"
            else:
                res[currIdx] = f"{i+1}"
        return res



