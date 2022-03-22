# 反转链表
# 思路：遍历这个链表，把这个链表中的每个值都存在一个数组里
# 再把数组中的值反转，再新建一个链表，依次把数组里的值取出来
# 最后把新建的链表返回即可

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 边界条件，如果链表为空，则返回None
        if not head:
            return head
        # 新建一个数组，用来存放链表中的值
        arr = []
        cur = head
        # 遍历链表，把每个节点的值存入数组
        while cur:
            arr.append(cur.val)
            cur = cur.next
        # 反转数组
        arr.reverse()
        # 新建一个链表
        new_head = ListNode(arr[0])
        cur = new_head
        # 把数组中的值依次添加到新建的链表中
        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return new_head