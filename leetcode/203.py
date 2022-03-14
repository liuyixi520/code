# 遍历整个链表，碰到目标值，就把当前节点的前一个节点的next指向当前节点的next，即可删除当前节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # head==None表示链表为空，这时返回False
        if not head:
            return head
        # 上一个节点
        pre = head
        # 当前节点
        cur = head.next
        while cur:
            # 如果当前节点的值等于目标值，则删除当前节点
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            # 否则，更新当前节点和上一个节点
            else:
                pre = cur
                cur = cur.next
        # 考虑到最后一个节点的情况，如果最后一个节点的值等于目标值，则删除最后一个节点
        if head.val == val:
            head = head.next
        return head 