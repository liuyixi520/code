# 自己的一些理解:
# 考虑使用栈这个数据结构来辅助实现这个算法
# 用一个标志位balanced来标识这个表达式是否是合法的，默认合法
# 初始化栈为空，从前往后便利这个栈，而且当前要是合法的表达式，来看是否是括号匹配的表达式
# 如果遇到左括号，那么就将当前这个符号压入栈内
# 碰到右括号时，首先检查当前栈是否为空，如果是，直接将标志位置为假
# 否则判定是否括号匹配，如果不匹配，那么也直接将标志位置为假
# 如果匹配，那么就将栈顶的元素弹出，开始检查下一个位置
####################################.
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return bool布尔型
#

class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        balanced = True
        ix = 0
        lst = []
        while balanced and ix < len(s):
            if s[ix] in '([{':
                lst.append(s[ix])
            # 其他的情况：)]}
            else:
                # 没有左括号与其匹配，这个括号字符串就是非法的
                if len(lst) == 0:
                    balanced = False
                else:
                    # 当前的符号不匹配
                    if not '([{'.index(lst.pop()) == ')]}'.index(s[ix]):
                        balanced = False
            ix = ix + 1 
        if balanced and len(lst)==0:
            return True
        else:
            return False
s = Solution()
print(s.isValid('()'))
            