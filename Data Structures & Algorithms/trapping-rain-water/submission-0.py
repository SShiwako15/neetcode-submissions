class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        p_max, s_max = 0, 0
        vol = 0
        for i in range(n):
            p_max = max(p_max, height[i])
            prefix[i] = p_max
        for i in range(n - 1, -1, -1):
            s_max = max(s_max, height[i])
            suffix[i] = s_max
        for i in range(n):
            vol += min(prefix[i], suffix[i]) - height[i]
        return vol