# 二叉树的最大深度
# 思路：递归。二叉树的最大深度为左右子树的最大深度加1。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 边界条件检查
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1