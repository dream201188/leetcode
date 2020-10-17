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
3因为多了一个min_path变量不太好理解了，改成不传递变量；
1 2 3版本思路是递归时候带着深度，在下潜过程中深度+1；
现在改成递归回溯过程深度+1，也就是冒泡过程+1；
这样整个过程更好理解一些；
"""


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            min_path = 10**9
            if root.left:
                min_path = min(min_path, dfs(root.left))
            if root.right:
                min_path = min(min_path, dfs(root.right))

            return min_path + 1

        return dfs(root)


# @lc code=end
