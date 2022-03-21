# 移除链表中的指定元素
# 遍历这个链表，判断下一个节点的值是否等于val，如果是，则删除这个节点，并将指针指向下一个节点
# 第一个元素没有进行判断，再把第一个元素进行判断补充

# 遍历整个链表，碰到目标值，就把当前节点的前一个节点的next指向当前节点的next，即可删除当前节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 边界条件，如果链表为空，那么就直接返回
        if not head:
            return head
        # 初始化一个指针，指向链表的头结点
        pre_node = head
        # 初始化一个指针，指向链表的头结点的下一个结点
        next_node = head.next
        # 如果当前节点的下一个结点的值等于val，那么就删除当前节点
        while next_node:
            # 如果下一个节点next_node的值是要删除的元素，那么就删除当前节点
            # 当前指针要后移两位
            if next_node.val == val:
                pre_node.next = next_node.next
            # 否则不用删除，只把当前指针后移一位即可
            else:
                pre_node = pre_node.next
            # 不管下一个节点的值是否是要删除的元素，都要把next_node后移一位
            next_node = next_node.next
        # 检查第一个元素是否是要删除的元素
        if head.val == val:
            return head.next
        return head