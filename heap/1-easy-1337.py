class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        from queue import PriorityQueue
        q = PriorityQueue(len(mat))
        for i, row in enumerate(mat):
            q.put((sum(row), i))
        res = []
        for _ in range(k):
            res.append(q.get())
        res = sorted(res)
        return list(map(lambda x: x[1], res))
