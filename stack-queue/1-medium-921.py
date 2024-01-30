class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if not stack:
                stack.append(p)
            else:
                if stack[-1] == "(" and p == ")":
                    stack.pop(-1)
                else:
                    stack.append(p)
        return len(stack) 
