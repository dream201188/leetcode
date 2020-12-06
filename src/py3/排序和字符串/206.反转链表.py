#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = head
        pre = None
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre

    def reverseList(self, head):
        if not head:
            return head
        node = head

        def dfs(node):
            if not node.next:
                return node
            tail = dfs(node.next)
            node.next.next = node
            return tail
        ans = dfs(node)
        head.next = None
        return ans

    """
    这种写法确实简单明了，每次都把当前node 指向None，
    其实只是需要最后一个指向
    """
    def reverseList(self, head):
        if not head or not head.next:
            return head
        node = head
        tail = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return tail




if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    node = head
    for i in range(2, 6):
        node.next = ListNode(i)
        node = node.next
    node.next = None
    s.reverseList(head)


# @lc code=end

