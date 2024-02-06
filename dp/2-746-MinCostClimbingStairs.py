class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = [-1] * len(cost)
        memory[0] = cost[0]
        memory[1] = cost[1]
        for i in range(2, len(cost)):
            memory[i] = cost[i] + min(memory[i-1], memory[i-2])
        return min(memory[-1], memory[-2])
