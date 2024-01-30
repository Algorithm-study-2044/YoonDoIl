class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def buildPQ(a):
            from queue import PriorityQueue
            q = PriorityQueue(len(nums))
            for num in a:
                if num:
                    q.put(num)
            return q

        currNums = nums
        numTrial = 0
        
        while sum(currNums) > 0:
            q = buildPQ(currNums)
            numTrial += 1
            currMin = q.get()
            for i in range(len(currNums)):
                if currNums[i]:
                    currNums[i] -= currMin
        return numTrial
                


        
