class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            temp = (n >> i) & 1
            rev += (temp << (31 - i))
        return rev