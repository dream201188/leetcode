# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans.reverse()
        return ans

    """
    递归
    """
    def __init__(self):
        self.ans = []
    def reversePrint(self, head):
        if not head:
            return self.ans

        self.reversePrint(head.next)
        self.ans.append(head.val)
        return self.ans

    def reversePrint(self, head):
        if not head:
            return []

        ans = self.reversePrint(head.next)
        return ans + [head.val]





