# 删除排序链表中的重复元素
# 思路：
# 题目中已经声明了链表中的元素是按照升序排列的
# 所以我们可以使用双指针，一个指向上一个节点pre，一个指向当前节点cur
# 如果下一个节点的值和当前节点的值相同，则删除下一个节点
# 如果下一个节点的值和当前节点的值不同，则将当前节点的next指向下一个节点
# 这个题目和删除链表中的指定元素有点类似

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 边界条件检查，如果链表为空，则返回None
        if not head:
            return head
        # 初始化两个指针pre和cur
        pre = head
        cur = head.next
        # 当cur不为空时，循环
        while cur:
            # 如果当前节点的值和上一个节点的值相同，则删除当前节点
            if cur.val == pre.val:
                pre.next = cur.next
            # 否则，上一个节点只需要后移一位即可
            else:
                pre = cur
            # 无论删不删除节点，都要把当前节点后移一位
            cur = cur.next
        return head