#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
将最大深度也上最小深度中的冒泡过程加1来一遍
"""


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            return max(left_depth, right_depth) + 1

        return dfs(root)


# @lc code=end
