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
                    
                    currrow = row.setdefault(i, set())
                    if board[i][j] in currrow:
                        return False
                    currrow.add(board[i][j])

                    currcol = col.setdefault(j, set())
                    if board[i][j] in currcol:
                        return False
                    currcol.add(board[i][j])
                    
                    currbox = box.setdefault((i//3,j//3), set())
                    if board[i][j] in currbox:
                        return False
                    currbox.add(board[i][j])
                    
        return True
