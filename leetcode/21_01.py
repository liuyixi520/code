# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 使用递归来解答
# 递归基：如果其中一个链表为空，那么就返回另一个
# 转移方程：不为空时，比较两个链表当前元素的值
# 如果list1.val比较小，那么就合并list1.next和list2，然后返回list1
# 反之list2.val比较小，那么就合并list2.next和list1，然后返回list2

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
