#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
第一个版本没有考考到没有左子树的情况；没有子树只能算别的
"""


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, depth=0):
            if not root:
                return depth
            return min(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


# @lc code=end
