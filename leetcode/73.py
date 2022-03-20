# 矩阵置零
# 思路：遍历矩阵，记住每个为零元素的坐标
# 然后将坐标中对应的行列所有元素都改为0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先遍历一遍矩阵，记录每个为零元素的坐标
        # 定义一个数组，数组里面的元素是元组，元组记录的是为零元素的行列坐标
        zero_pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_pos.append((i, j))
        # 然后将坐标中对应的行列所有元素都改为0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in zero_pos:
                    # 将行上的元素都改为0
                    matrix[i] = [0] * len(matrix[0])
                    # 将列上的元素都改为0
                    for k in range(len(matrix)):
                        matrix[k][j] = 0