#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, level, index = [], [root], 0
        while level:
            pairs = [(node.left, node.right) for node in level]
            # level = level[::-1] if index % 2 else level
            if index % 2:
                level.reverse()  # 这没有返回值，不能进行迭代
            ans.append([node.val for node in level])
            index = index + 1
            level = [node for pair in pairs for node in pair if node]
        return ans


# @lc code=end
