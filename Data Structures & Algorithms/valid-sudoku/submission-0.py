class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        vertical = [] * 9
        horizontal = [] * 9
        grid = [] * 9

        vert = 0
        hor = 0
        current = board[0][0]

        for i in range(9):
            for j in range(9):
                vertical = []
                horizontal = []
                grid = []
                
                for k in range(9):
                    if(board[i][k] !='.'):
                        vertical.append(board[i][k])
                    if(board[k][j] !='.'):
                        horizontal.append(board[k][j])
                
                if(vertical.count(board[i][j]) > 1 or horizontal.count(board[i][j]) > 1):
                    return False
                l = int(i/3) * 3
                for l in range(l, l+3):
                    m = int(j/3) * 3
                    for m in range (m, m+ 3):
                        print(l,m,board[l][m])
                        if(board[l][m] !='.'):
                            grid.append(board[l][m])
                if(grid.count(board[i][j]) > 1):
                    return False
                

        
        return True

                    

        