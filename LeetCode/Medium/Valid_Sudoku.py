'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValidBlock(row):
                return False
        for i in range(9):
            col = ''
            col = [col + row[i] for row in board]
            if not self.isValidBlock(''.join(col)):
                return False
        
        for i in range(3):
            for j in range(3):
                b = ''
                b = [''.join(board[i * 3 + m][j * 3:j * 3 + 3]) for m in range(3)]
                if not self.isValidBlock(''.join(b)):
                    return False
        return True
    
    def isValidBlock(self, block):
        dic = collections.Counter(block)
        for k,v in dic.items():
            if v > 1 and k != '.':
                return False
        return True