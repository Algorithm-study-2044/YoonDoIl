class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverseTree(node):
            if node:
                return [node.val] + traverseTree(node.left) + traverseTree(node.right)
            else:
                return []
        from collections import Counter
        values = traverseTree(root)
        valueCounts = Counter(values).most_common()
        maxCount = valueCounts[0][1]
        return list(map(lambda x: x[0],filter(lambda x: x[1] == maxCount, valueCounts)))
