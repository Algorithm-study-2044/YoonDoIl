class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = []
        tl = []
        for c in s:
            if c == "#":
                if sl:
                    sl.pop(-1)
            else:
                sl.append(c)
        for c in t:
            if c == "#":
                if tl:
                    tl.pop(-1)
            else:
                tl.append(c)
        return sl == tl
        
