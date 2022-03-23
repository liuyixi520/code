# 二叉树层序遍历
# 这棵树在便利的时候是从上到下，从左到右，这样的遍历方式是按层序遍历的
# 所以使用一个队列和数组来实现
# 首先检测边界条件，如果是空树，直接返回空数组
# 然后将根节点入队
# 这个队列如果不为空的时候就开始执行下面的循环
#   将队列中的第一个元素添加到数组中
#   如果这个元素的左子节点不为空，将其左子节点入队
#   如果这个元素的右子节点不为空，将其右子节点入队
#   将队列中的第一个元素出队

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 如果这棵树是空的，那么返回一个空的列表
        if not root:
            return []
        # 定义返回的列表
        res = []
        # 定义队列，这个队列中存放的是树的节点
        queue = []
        # 将根节点添加到队列中
        queue.append(root)
        # 当队列不为空时
        while queue:
            # 获得当前队列长度，即当前层的节点数
            size = len(queue)
            # 定义一个数组，用来存放当前层的节点
            temp = []
            for _ in range(size):
                # 如果左子树不为空，那么将左子树添加到队列中
                if queue[0].left:
                    queue.append(queue[0].left)
                # 如果右子树不为空，那么将右子树添加到队列中
                if queue[0].right:
                    queue.append(queue[0].right)
                # 这是不带括号的分层来实现的，比较简单
                temp.append(queue[0].val)
                queue.pop(0)
            res.append(temp)
        return res
