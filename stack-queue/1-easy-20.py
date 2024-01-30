class Solution:
    def isValid(self, s: str) -> bool:
        left = ('(', '[', '{')
        right = (')', ']', '}')
        pairs = {')':'(',']':'[', '}':'{'}
        stack = []
        for char in s:
            if not stack or (char in left):
                stack.append(char)
            else:
                if stack[-1]  == pairs[char]:
                    stack.pop()
                else:
                    stack.append(char)
        return not bool(len(stack))
