# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []  # 每次进来先拿到一层的数量
            for i in range(len(queue)):  # 获取size，还是用len(queue)
                tmp = queue.popleft()
                level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            ans.append(level)  # 每一层一个新的level，添加到结果里面
        return ans

    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:  # 上一层的旧level
            ans.append([node.val for node in level])  # 不再显示用queue，level每次都是新的
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]  # 新的level
        return ans

    """
    3与2思路一样，唯一不同是以元组进入，后面双for循环加if判断
    """

    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])  # 不再显示用queue，level每次都是新的
            tmp = ([(node.left, node.right) for node in level])
            level = [node for pair in tmp for node in pair if node]
        return ans
