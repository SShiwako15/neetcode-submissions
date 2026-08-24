class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                topIdx,topVal = stack.pop()
                area = topVal * (i - topIdx)
                maxArea = max(maxArea, area)
                start = topIdx
            stack.append([start,v])
        while stack:
            topIdx,topVal = stack.pop()
            area = topVal * (n - topIdx)
            maxArea = max(maxArea, area)
        return maxArea