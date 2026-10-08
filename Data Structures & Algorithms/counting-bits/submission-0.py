class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def count1(n: int) -> int:
            count = 0
            while n:
                count += 1
                n = n & (n - 1)
            return count
        for i in range(n + 1):
            output.append(count1(i))
        return output