#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
纯自己实现版本：
1.第一种办法是严格按照定义来验证，但是不好判断整个右子树都大于根节点；
2.第二种办法使用的中序遍历，然后判断结果是不是严格升序的；判断过程完全自己写；
"""


class Solution(object):

    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True

    #     if root.left and root.left.val >= root.val:
    #         return False
    #     if root.right and root.right.val <= root.val:
    #         return False

    #     left = self.isValidBST(root.left)
    #     right = self.isValidBST(root.right)
    #     return left and right

    def isValidBST(self, root):

        order_list = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            order_list.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(len(order_list) - 1):
            if order_list[i] >= order_list[i + 1]:
                return False

        return True


# @lc code=end
