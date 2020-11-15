class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3 ) * 3 + j // 3].remove(val)

        def dfs(index = 0):
            if index == len(empty):
                return True

            i, j = empty[index]
            b = (i // 3 ) * 3 + j // 3

            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if dfs(index + 1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
                board[i][j] = '.'
            return False

        dfs(0)
if __name__ == "__main__":
    s = Solution()
    s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

