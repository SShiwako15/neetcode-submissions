class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hs = set()
        curr = 0
        i,j = 0, 0
        while j < len(s):
            while s[j] in hs:
                hs.remove(s[i])
                i += 1
                curr -= 1
            hs.add(s[j])
            j += 1
            curr += 1
            longest = max(longest, curr)
        return longest