from itertools import combinations
from collections import defaultdict, Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sum_dict = defaultdict(list)
        for pair in combinations(nums, 2):
            sum_dict[sum(pair)].append(pair)
        
        res = set()
        for pair in combinations(nums, 2):
            curr_sum = sum(pair)
            target_sum = target - curr_sum
            if target_sum == curr_sum:
                sum_dict[target_sum].remove(pair)
                for s in sum_dict[target_sum]:
                    res.add(tuple(sorted([*pair, *s])))
                sum_dict[target_sum].append(pair)
            else:
                for s in sum_dict[target_sum]:
                    res.add(tuple(sorted([*pair, *s])))
        
        input_counter = Counter(nums)
        
        res = list(res)
        result = []
        for quad in res:
            c = Counter(quad)
            flag = True
            for k,v in c.items():
                if v > input_counter[k]:
                    flag = False
                    break
            if flag:
                result.append(list(quad))
        return result
                
