# 对称二叉树
# 思路：递归
# 如果是个对称树，那么左子树和右子树都是对称的
# 也就是说左子树的根节点和右子树的根节点是相等的
# 而且左子树的左子树和右子树的右子树是相等的
# 左子树的右子树和右子树的左子树是相等的
# 递归基：
# 如果两个树都是空树，那么返回True
# 如果有一个树不是空树，那么返回False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 边界条件，如果是空树，那么返回True
        if not root:
            return True
        left_node = root.left
        right_node = root.right
        return self.is_sysm(left_node, right_node)

    # 判断两棵树是否对称
    def is_sysm(self, root1, root2):
        # 如果两个树都是空树，那么返回True
        if not root1 and not root2:
            return True
        # 如果有一个树不是空树，那么返回False
        # 这里有个小逻辑，上面已经判定了两个树都不是空树
        # 所以这里要成立，必定只有一个树不是空树
        if not root1 or not root2:
            return False
        # 如果两个树的值不相等，那么返回False
        if root1.val != root2.val:
            return False
        # 如果两个树的值相等，那么返回左子树和右子树是否对称
        return self.is_sysm(root1.left, root2.right) and self.is_sysm(root1.right, root2.left)
        