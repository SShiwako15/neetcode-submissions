class Solution:
    def vert_search(self, matrix: List[List[int]], target: int, h: int, l: int, r: int) -> bool:
        if l > r:
            return False
        m = l + (r - l) // 2
        mid = matrix[h][m]
        
        if mid == target:
            return True
        if mid > target:
            return self.vert_search(matrix, target, h, l, m - 1)
        return self.vert_search(matrix, target, h, m + 1, r)

    def hor_search(self, matrix: List[List[int]], target: int, l: int, r: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2
        if matrix[m][0] <= target <= matrix[m][len(matrix[0]) - 1]:
            return m
        elif target < matrix[m][0]:
            return self.hor_search(matrix, target, l, m - 1)
        return self.hor_search(matrix, target, m + 1, r)



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        l = 0
        b = len(matrix) - 1
        r = len(matrix[0]) - 1
        h = self.hor_search(matrix, target, t, b)
        if h == -1:
            return False
        return self.vert_search(matrix, target, h, l, r)
        