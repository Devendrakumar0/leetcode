class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        c = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                c+= 1
                i += 1
            j += 1
        return c
