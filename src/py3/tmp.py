class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
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
                if node.righ: queue.append(node.right)
        return True


if __name__ == "__main__":
    [1,2,2,3,4,4,3]
    root11 = root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    tmp = root
    root = root.left
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root = tmp.right
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    s = Solution()
    s.isSymmetric(root11)






