# 有效的括号
# 使用栈这个数据结构，碰到左括号就压入栈，碰到右括号就弹出栈顶元素
# 如果栈为空或者指定元素与当前括号不匹配，则返回False
# 如果便利完整个字符串，栈为空，则返回True

class Solution:
    def isValid(self, s: str) -> bool:
        # 创建一个栈，使用list来实现，append为入栈，pop为出栈
        stack = []
        # 创建一个字典，用于存储括号的对应关系
        dic = {'(':')', '{':'}', '[':']'}
        # 遍历字符串
        for c in s:
            # 如果是左括号，就压入栈
            if c in dic:
                stack.append(c)
            # 如果是右括号，则弹出栈顶元素
            else:
                # 如果栈为空，则返回False
                if not stack:
                    return False
                # 如果栈顶元素和当前括号不匹配，则返回False
                if dic[stack.pop()] != c:
                    return False
        # 如果遍历完字符串，栈为空，则返回True
        return not stack
