# 哪有那么多奇技淫巧，本质上就是把所有可行解暴力穷举出来，然后从中找到一个最优解罢了。
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        used = set()

        cnt = -1
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index('0'))]

        while q:
            cnt += 1
            new = []
            for s, i in q:
                used.add(s)
                if s == '123450':
                    return cnt
                arr = [c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = ''.join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
            q = new

        return -1
