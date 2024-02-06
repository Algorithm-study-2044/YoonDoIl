class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        num_str = 0
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[len(stack)-1] != s[i]:
                    stack.pop()
                    if len(stack) == 0:
                        num_str += 1
                else:
                    stack.append(s[i])
        return num_str
