#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#


# @lc code=start
class Solution(object):

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        if not commands:
            return 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        dr = 0
        ans = 0
        cx, cy = 0, 0
        ot = set([(tmp[0], tmp[1]) for tmp in obstacles])
        for cm in commands:
            if cm == -1:
                dr = (dr + 1) % 4
            if cm == -2:
                dr = (dr + 3) % 4
            else:
                for i in range(cm):
                    if (cx + dx[dr], cy + dy[dr]) not in ot:
                        cx = cx + dx[dr]
                        cy = cy + dy[dr]
                        ans = max(ans, cx * cx + cy * cy)
                    else:
                        break
        return ans


# @lc code=end
