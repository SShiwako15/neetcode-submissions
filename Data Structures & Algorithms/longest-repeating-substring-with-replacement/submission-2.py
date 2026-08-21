import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        hs = {i: 0 for i in string.ascii_uppercase}
        for r in range(len(s)):
            hs[s[r]] += 1
            while r - l + 1 - max(hs.values()) > k:
                hs[s[l]] -= 1
                l += 1
            max_len = max(r - l + 1, max_len)
        return max_len
