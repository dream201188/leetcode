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


class Solution(object):

    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])  # 不再显示用queue，level每次都是新的
            tmp = ([(node.left, node.right) for node in level])
            level = [node for pair in tmp for node in pair if node]
        return ans


# @lc code=end
