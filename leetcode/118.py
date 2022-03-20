# 杨辉三角
# 规律：下面的一行总比上面一行多一个数字
# 而且下面的数字都是上面的数字临近的两个数字加出来的
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            # 先初始化当前的一行，有i+1个元素
            row = [1] * (i + 1)
            # 如果不是前两行，就需要把上一行的数字临近的两个数字加出来
            # 这样很巧妙的避开了当前行第一个元素和最后一个元素的初始化
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res