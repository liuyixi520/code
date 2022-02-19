#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        res = []
        res.append(1)
        res.append(1)
        for i in range(2, number+1):
            res.append(res[i-1] + res[i-2])
        return res[number]
# sol = Solution()
# print(sol.jumpFloor(7))