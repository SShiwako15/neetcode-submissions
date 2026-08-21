class Solution:
    def clean(self, s:str) -> str:
        out = ""
        for i in s:
            if i.isalnum():
                out += i.lower()
        return out
        
    def isPalindrome(self, s: str) -> bool:
        s_clean = self.clean(s)
        fr = 0
        bk = len(s_clean) - 1
        while fr <= bk:
            if s_clean[fr]!= s_clean[bk]:
                return False
            fr += 1
            bk -= 1
        return True