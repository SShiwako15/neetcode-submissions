class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        out = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temp[j] <= temp[i]:
                if out[j] == 0:
                    j = n
                else:
                    j += out[j]
            if j < n:
                out[i] = j - i
        return out
