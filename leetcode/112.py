# 路径总和
# 思路：关键是要判断是否是叶子节点，如果是叶子节点，则直接加上当前节点的值，如果不是叶子节点，则递归调用

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            