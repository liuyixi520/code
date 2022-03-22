# 二叉树的前序遍历
# 先序遍历：根节点->左子树->右子树
# 直到当前的节点为空，返回
# 使用递归的手段，来实现上述过程
# 备注：题目中的二叉树案例是用数组表示的，它是按照一层一层累计表示下来的，碰到空节点就用null填充

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # 如果当前节点为空，返回
        if not root:
            return []
        res.append(root.val)
        # 先遍历左子树，再遍历右子树
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
