#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []  # 每次进来先拿到一层的数量
            for i in range(len(queue)):  # 获取size，还是用len(queue)
                tmp = queue.popleft()
                level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            ans.append(level)  # 每一层一个新的level，添加到结果里面
        return ans


# @lc code=end
