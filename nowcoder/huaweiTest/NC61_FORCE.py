#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
# 备注：暴力解法超出时间限制了
class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        # write code here
        n = len(numbers)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                if(numbers[i] + numbers[j] == target):
                    res.append(i)
                    res.append(j)
                    return res