class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substr = [0,0]
        strlen = float("inf")
        curr = 0
        if len(s) < len(t):
            return ""
        l = 0
        tset = Counter(t)
        sset = Counter()
        for r in range(len(s)):
            c = s[r]
            sset[c] += 1
            if c in t and sset[c] == tset[c]:
                curr += 1
            
            while curr == len(tset):
                d = s[l]
                if d in t and sset[d] == tset[d]:
                    if (r - l + 1 < strlen):
                        substr = [l, r]
                        strlen = r - l + 1
                    curr -= 1
                sset[d] -= 1
                l += 1
        return s[substr[0] : substr[1] + 1] if strlen != float("inf") else ""