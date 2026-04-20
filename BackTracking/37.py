class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        # precompute whole sudoku
        # row wise, col wise, and block wise
        # for O(1) lookup

        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        blk_sets = [set() for _ in range(9)]
        empties = set()
        DIGITS = '123456789'

        # find empties
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.add((r, c))
            

        for col in range(9):
            for row in range(9):

                if board[row][col] == '.':
                    continue
                
                value = board[row][col]
                blk = (row//3)*3 + col//3

                row_sets[row].add(value)
                col_sets[col].add(value)
                blk_sets[blk].add(value)
        
        def issafe(num, r, c):
            index = (r//3) * 3 + (c//3)
            if num not in row_sets[r] and num not in col_sets[c] and num not in blk_sets[index]:
                return True
            return False

        def solve():

            # calculate the mrv for the whole sudoku 
            # solve for the output and solve again
            # until solved all and return True

            best_candidate = None
            best_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            best_len = 10

            for candidate in empties:
                row, col = candidate
                options = [place for place in DIGITS if issafe(place, row, col)]
                if not options:
                    return False

                if len(options) < best_len:
                    best_len = len(options)
                    best_options = options
                    best_candidate = candidate
            
            if best_candidate == None:
                return True

            for place in best_options:
                
                row, col = best_candidate
                blk = (row//3) * 3 + (col//3)

                # backtracking
                row_sets[row].add(place)
                col_sets[col].add(place)
                blk_sets[blk].add(place)
                empties.remove(best_candidate)

                board[row][col] = place
                
                if solve():
                    return True

                board[row][col] = '.'
            
                empties.add(best_candidate)
                row_sets[row].remove(place)
                col_sets[col].remove(place)
                blk_sets[blk].remove(place)

            return False
        solve()





            


            
