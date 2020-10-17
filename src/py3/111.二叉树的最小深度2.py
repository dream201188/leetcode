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
在1的基础上完善，把深度为0 独立出去；
全没有子树则是当前深度；
只有左子树那以左子树为准；
只有右子树以右子树为准；
左右都有取最小值；

1版本的话如果没有左子树，默认左子树算1了，与题意中求叶子节点深度不符合；
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

            if root.left and not root.right:
                return dfs(root.left, depth + 1)
            if root.right and not root.left:
                return dfs(root.right, depth + 1)
            else:
                return min(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 1)


# @lc code=end
