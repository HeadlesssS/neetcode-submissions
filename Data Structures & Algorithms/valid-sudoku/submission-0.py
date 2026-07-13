class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #checking lists directly
        j=0
        while j<9:
            cube=[]
            k=0
            rows=[]
            columns=[]
            #rowcheck
            for i in board[j]:
                if i in rows:
                    if i!=".":
                        return False
                elif i not in rows:
                    rows.append(i)
                    
            #columncheck
            for i in board:
                if board[k][j] in columns:
                    if board[k][j]!=".":
                        return False
                else:
                    columns.append(board[k][j])
                k+=1

            j+=1
        


        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                cube = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            if val in cube:
                                return False
                            cube.append(val)
        return True
                

