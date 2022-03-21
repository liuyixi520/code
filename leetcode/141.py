# 环形链表
# 使用快慢指针，快指针每次走两步，慢指针每次走一步
# 如果有环，快慢指针会相遇，否则不会相遇
# 这样来设计循环：如果快指针没有走到结尾，那么就一直循环下去
# 把慢指针放在头结点上，快指针放在头节点后面的那个节点上
# 如果快慢指针相遇了，说明这个链表有环，返回True
# 否则快指针走两步，慢指针走一步

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 边界条件，如果链表为空，或者只有一个节点，那么就不存在环
        # python中的None是一个特殊的类型，表示空值，用布尔值False表示
        if not head or not head.next:
            return False
        # 初始化快慢指针
        slow = head
        fast = head.next
        # 如果快指针没有走到尾部，那么就一直走
        while fast and fast.next:
            # 如果快慢指针相遇，那么就存在环
            if slow == fast:
                return True
            # 快指针每次走两步，慢指针每次走一步
            slow = slow.next
            fast = fast.next.next
        # 如果快指针没有走到尾部，那么就不存在环
        return False