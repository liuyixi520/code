# 自顶向下，直接使用暴力递归的方式，注意递归的三个要素
# 1. 递归基
# 2. 要向递归基靠近
# 3. 要自己调用自己

class Solution:
    def climbStairs(self, n: int) -> int:
        # 自定义一个函数，使用一个mem数组，用来记录已经计算过的楼梯阶数
        # 避免常规的递归会重复计算
        def dfs(i: int, mem) -> int:
            if mem[i] != -1:
                return mem[i]
            else:
                if i==0 or i==1:
                    return 1
                else:
                    mem[i] = dfs(i-1, mem) + dfs(i-2, mem)
                    return mem[i]
        return dfs(n, [-1]*(n+1))

s = Solution()
print(s.climbStairs(5))