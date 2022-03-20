# 矩阵的重塑
# 给定一个矩阵mxn，然后将它变换成一个rxc的矩阵
# 思路：先将这个矩阵拉平flatten，然后再输出成一个rxc的矩阵
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 如果转换的格式非法，就直接返回原来的矩阵
        if r * c != len(mat) * len(mat[0]):
            return mat
        res = []
        # 先将矩阵拉平
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res.append(mat[i][j])
        # [i*c : (i+1)*c]返回的是这个矩阵的第i行的所有元素
        # 依次循环下去就可以把这个矩阵构造出来了
        res = [res[i * c:(i + 1) * c] for i in range(r)]
        return res