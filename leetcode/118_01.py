# 记i为行数，j为列数
# 第i行的数据是由i-1行的元素构成的
# 第j列的数据是由第上一行的j和j-1列构成的，由下标为1的列开始计算
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0: return [[]]
        elif numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1,1]]
        else:
            res = [[1], [1,1]]
            for i in range(2, numRows):
                tmp = [1]
                for j in range(1, i):
                    tmp.append(res[i-1][j-1]+res[i-1][j])
                tmp.append(1)
                res.append(tmp)
            return res