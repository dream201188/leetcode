class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = list()
        stack.append(-1)
        max_ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                stack.pop()
                if 0 == len(stack):
                    stack.append(i)
                if 0 < len(stack):
                    max_ans = max(max_ans, i - stack[-1])
        return max_ans
