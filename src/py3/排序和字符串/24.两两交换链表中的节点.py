#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node = head
        pre = ListNode(0)
        pre.next = head
        head = node.next
        while node and node.next:
            pre.next = node.next
            pre = node
            tmp = node.next.next
            node.next.next = node
            node.next = tmp
            node = tmp
        return head





# @lc code=end

