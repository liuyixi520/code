# 有效的数独
# 暴力法：先判断行，再判断列，再判断3*3的小方格
# 时间复杂度：O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 判断行
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
        # 判断列
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col:
                        return False
                    else:
                        col.add(board[i][j])
        # 判断3*3的小方格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] != '.':
                            if board[m][n] in box:
                                return False
                            else:
                                box.add(board[m][n])
        return True