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
2分四种情况比较啰嗦，通过一个中间变量min_path，省略了两个都有的情况；
"""


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        def dfs(root, depth=0):
            if not root.left and not root.right:
                return depth

            min_path = 10**9
            if root.left:
                min_path = min(min_path, dfs(root.left, depth + 1))
            if root.right:
                min_path = min(min_path, dfs(root.right, depth + 1))

            return min_path

        return dfs(root, 1)


# @lc code=end
