class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            s= set()
            for j in range(9):
                item = board[i][j]
                if item  in s:
                    return False
                elif item != '.':
                    s.add(item)
        #col
        for i in range(9):
            s= set()
            for j in range(9):
                item = board[j][i]
                if item  in s:
                    return False
                elif item != '.':
                    s.add(item)

        #box
        start =[(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]

        for i,j in start:
            s = set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    item = board[r][c]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        
        return True

