# 用栈实现队列
# 要求实现队列中的基本操作：push、pop、peek、empty
# 思路：
# 栈是一种先入后出的LIFO（Last In First Out）数据结构，队列是一种先入先出的FIFO（First In First Out）数据结构。
# 如果使用栈来模拟队列，就需要两个栈，一个用来存放队列的数据，一个用来协助操作。

class MyQueue:

    def __init__(self):
        # 初始化两个栈
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # 将stack1中的元素压入stack2中
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 将x压入stack1中
        self.stack1.append(x)
        # 将stack2中的元素压入stack1中
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        # 直接弹出stack1的栈顶元素
        return self.stack1.pop()

    def peek(self) -> int:
        # 直接返回stack1的栈顶元素
        return self.stack1[-1]

    def empty(self) -> bool:
        # 如果stack1为空，则返回True
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
