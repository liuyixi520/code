class Solution:
    def fib(self, n: int) -> int:
        def dfs(i: int, mem):
            if mem[i] != -1:
                return mem[i]
            else:
                if i==0 or i==1:
                    return i
                else:
                    mem[i] = dfs(i-1, mem) + dfs(i-2, mem)
                    return mem[i]
        return dfs(n, [-1]*(n+1))%1000000007

s = Solution()
print(s.fib(5))