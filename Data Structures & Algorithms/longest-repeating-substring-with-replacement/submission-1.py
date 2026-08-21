import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        curr = 0
        hs = {i: 0 for i in string.ascii_uppercase}
        while r < len(s):
            hs[s[r]] += 1
            curr += 1
            while curr - max(hs.values()) > k:
                hs[s[l]] -= 1
                curr -= 1
                l += 1
            r += 1
            max_len = max(curr, max_len)
        return max_len
