# 二叉树中序遍历
# 先中后的顺序是相对于根节点来说的，而且左节点始终在前，右节点在后
# 中序遍历：左->中->右
# 思路：递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 定义返回数组
        res = []
        # 定义递归终止条件
        if not root:
            return []
        # 先遍历左子树，再遍历右子树
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res