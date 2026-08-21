class Solution:
    def validityCheck(self, nums: List[str]) -> bool:
        digits = []
        for i in nums:
            if i == ".":
                continue
            if i in digits:
                return False
            
            digits.append(i)
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.validityCheck(board[i]):
                return False
            if not self.validityCheck([row[i] for row in board]):
                return False
            temp = []
            for a in range(3):
                for b in range(3):
                    row = (i // 3) * 3 + a
                    col = (i % 3) * 3 + b
                    temp.append(board[row][col])
            if not self.validityCheck(temp):
                return False

        return True