#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
我认为这是最难写的迭代办法写后序遍历，没有取巧：用stack保存遍历过但是还不需要添加的节点，弹出后判断
右儿子的情况，（如果没有右儿子或者右儿子是刚刚添加的节点，那么该节点可以添加）或者 用（有右儿子并且右儿子不是刚访问的，
那么就不能弹出这个节点，要继续访问该节点右儿子）
"""


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        prev = None

        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            if tmp.right and tmp.right != prev:  #有右儿子并且右儿子不是刚访问的，
                #那么就不能弹出这个节点，要继续访问该节点右儿子
                cur = tmp.right
                stack.append(tmp)
            else:
                res.append(tmp.val)
                prev = tmp
        return res


# @lc code=end
