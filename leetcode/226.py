# 翻转二叉树
# 思路：递归
# 递归基：当节点为空时，返回空
# 递归规则：
# 1. 左子树翻转
# 2. 右子树翻转
# 3. 左右子树交换
# 4. 返回根节点


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 边界条件，如果树为空，返回空
        if not root:
            return None
        # 左子树翻转
        left = self.invertTree(root.left)
        # 右子树翻转
        right = self.invertTree(root.right)
        # 左右子树交换
        root.left, root.right = right, left
        return root