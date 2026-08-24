class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                topTemp, topIdx = stack.pop()
                out[topIdx] = idx - topIdx
            stack.append([temp, idx])
        return out