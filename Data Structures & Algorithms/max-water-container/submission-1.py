class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f, b = 0, len(heights) - 1
        maxarea = 0
        while f < b:
            area = (b - f) * min(heights[f], heights[b])
            maxarea = max(area, maxarea)
            if heights[f] < heights[b]:
                f += 1
            else:
                b -= 1
        return maxarea