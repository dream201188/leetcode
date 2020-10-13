#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def postorderTraversal(self, root):
        res = []
        stack = list()
        prev = None
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            tmp = stack.pop()
            if not tmp.right or tmp.right == prev:  #如果没有右儿子或者右儿子是刚刚添加的节点，那么该节点可以添加
                res.append(tmp.val)
                prev = tmp
            else:
                cur = tmp.right
                stack.append(tmp)
        return res


# @lc code=end
