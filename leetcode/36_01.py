class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 检查行上的合法性
        for i in range(9):
            s = set()
            l = list()
            for j in range(9):
                if board[i][j] != '.':
                    s.add(board[i][j])
                    l.append(board[i][j])
                if(len(s) != len(l)):
                    return False 
        # 检查列上的合法性
        for j in range(9):
            s = set()
            l = list()
            for i in range(9):
                if board[i][j] != '.':
                    s.add(board[i][j])
                    l.append(board[i][j])
                if(len(s) != len(l)):
                    return False
        # 检查九宫格上的合法性
        for i in range(3):
            for j in range(3):
                s = set()
                l = list()
                for k in range(3):
                    for m in range(3):
                        if board[i*3+k][j*3+m] != '.':
                            s.add(board[i*3+k][j*3+m])
                            l.append(board[i*3+k][j*3+m])
                if(len(s) != len(l)):
                    return False
        return True