#
# [111] 二叉树的最小深度
#
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
第一个版本没有考考到没有左子树的情况；没有子树只能算别的
"""
class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, depth=0):
            if not root:
                return depth
            return min(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


"""
在1的基础上完善，把深度为0 独立出去；
全没有子树则是当前深度；
只有左子树那以左子树为准；
只有右子树以右子树为准；
左右都有取最小值；

1版本的话如果没有左子树，默认左子树算1了，与题意中求叶子节点深度不符合；
"""

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


"""
2分四种情况比较啰嗦，通过一个中间变量min_path，省略了两个都有的情况；
"""
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

"""
3因为多了一个min_path变量不太好理解了，改成不传递变量；
1 2 3版本思路是递归时候带着深度，在下潜过程中深度+1；
现在改成递归回溯过程深度+1，也就是冒泡过程+1；
这样的话容易找到最优子结构，上面的每个最先深度都是两个中最小一个加1
"""
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
