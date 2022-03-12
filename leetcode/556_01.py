# 将数组变换成一维数组，做flaten操作
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        res = [[0 for _ in range(c)] for _ in range(r)]
        for x in range(m*n):
            res[x//c][x%c] = mat[x//n][x%n]
        return res