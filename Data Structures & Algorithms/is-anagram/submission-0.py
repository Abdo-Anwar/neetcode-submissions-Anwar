class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        f=True
        for i in range(len(s_sorted)) :
            if s_sorted[i] != t_sorted[i]:
                f = False
        return f 