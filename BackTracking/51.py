# I have tried understanding the code and managed to understand about 50% of it
# there are many ways to implement this problem
# but I found this the most fascinating and optimized
# it was also easy to understand

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # this store the value
        res = []
        cols = [-1] * n

        # output generation 
        def gen_out():
            board = []
            for i in range(n):
                board.append(
                    '.' * (cols[i]) +
                    'Q' +
                    '.' * (n - 1 - cols[i])
                )
            return board

        # valid placement checker
        def check_safe_placement(row, col):

            for i in range(row):
                if col == cols[i]:
                    return False
                if abs(col - cols[i]) == abs(row - i):
                    return False
            return True

        # valid board generator using backtracking
        def generate(row_num):
            if row_num == n:
                res.append(gen_out())
                return
            
            for col in range(n):
                if check_safe_placement(row_num, col):
                    cols[row_num] = col
                    generate(row_num + 1)
                    cols[row_num] = -1
            
        generate(0)
        return res
