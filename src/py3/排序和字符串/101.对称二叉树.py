#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



import collections


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque([root])
        while queue:
            i, j = 0, len(queue) - 1
            while -1 < i <= j < len(queue):
                if queue[i].left and queue[j].right:
                    if queue[i].left.val != queue[j].right.val:
                        return False
                elif queue[i].left: return False
                elif queue[j].right: return False

                if queue[i].right and queue[j].left:
                    if queue[i].right.val != queue[j].left.val:
                        return False
                elif queue[i].right: return False
                elif queue[j].left: return False
                i += 1; j-= 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True


# @lc code=end

