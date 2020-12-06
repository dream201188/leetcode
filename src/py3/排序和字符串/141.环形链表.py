#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

    """
    快慢指针，相遇就有环，不相遇碰到None报错就没环
    """
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    """
    同样是快慢指针，上面异常处理方法更巧妙；简单好理解
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True



# @lc code=end

