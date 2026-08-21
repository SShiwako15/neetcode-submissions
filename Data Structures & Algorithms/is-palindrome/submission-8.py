class Solution:        
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        fr = 0
        bk = len(s) - 1
        while fr < bk:
            f = s[fr]
            b = s[bk]
            if not f.isalnum():
                fr += 1
            elif not b.isalnum():
                bk -= 1
            else:
                if f != b:
                    return False
                fr += 1
                bk -= 1
        return True