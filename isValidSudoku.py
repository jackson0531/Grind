# every column, row and subbox has to be uniquef
# insert unique tuples into set and if ever a duplicate we the return false
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        mySet = set()
        for i in range(len(board)): # row
            for j in range(len(board[0])): # col
                curr = board[i][j]
                if curr==".":
                    continue
                if ((i, curr) in mySet) or ((curr, j) in mySet) or ((i//3, j//3, curr) in mySet):
                    return False 
                mySet.add((i, curr))
                mySet.add((curr, j))
                mySet.add((i//3, j//3, curr))
        return True
