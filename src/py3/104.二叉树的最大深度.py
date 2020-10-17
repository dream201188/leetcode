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


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, depth=0):
            if not root:
                return depth
            depth = depth + 1
            left_depth = dfs(root.left, depth)
            right_depth = dfs(root.right, depth)
            return max(left_depth, right_depth)

        return dfs(root, 0)


# @lc code=end
