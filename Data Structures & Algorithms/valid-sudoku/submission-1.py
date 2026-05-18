class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                else:
                    
                    currrow = row.setdefault(i, {})
                    currrow[board[i][j]] = currrow.get(board[i][j], 0) + 1
                    currcol = col.setdefault(j, {})
                    currcol[board[i][j]] = currcol.get(board[i][j], 0) + 1
                    
                    currbox = box.setdefault((i//3,j//3), {})
                    currbox[board[i][j]] = currbox.get(board[i][j], 0) + 1
                    if currcol[board[i][j]] > 1:
                        return False
                    if currrow[board[i][j]] > 1:
                        return False
                    
                    if currbox.get(board[i][j]) > 1:
                        return False
        return True
