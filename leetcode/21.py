# 合并两个有序的链表
# 使用两个指针，一个指向第一个链表，一个指向第二个链表
# 新建一个链表，用来存放合并后的链表
# 判断两个指针指向的值，较小的放入新链表，并将指针后移
# 如果有一个链表为空时，将这个链表剩下的部分拷贝到新链表中即可

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 边界条件，如果有其中的一个链表为空，那么就直接返回另一个链表
        if not list1:
            return list2
        if not list2:
            return list1
        # 初始化两个链表的指针
        p1 = list1
        p2 = list2
        # 新建一个链表，用来存放合并后的链表
        new_list = ListNode(0)
        # 把这个新链表的头结点复制出来，用来存储操作过程的链表
        p = new_list
        # 如果有一个指针没有跑完，就一直跑
        while p1 and p2:
            # 如果p1指向的值小于p2指向的值，那么就把p1指向的值放入新链表
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            # 否则就把p2指向的值放入新链表
            else:
                p.next = p2
                p2 = p2.next
            # 把新链表的指针后移
            p = p.next
        # 如果p1指向的值还没有跑完，那么就把p1指向的值放入新链表
        if p1:
            p.next = p1
        # 如果p2指向的值还没有跑完，那么就把p2指向的值放入新链表
        if p2:
            p.next = p2
        # 返回新链表
        return new_list.next