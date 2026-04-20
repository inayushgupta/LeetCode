class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        intermediate = []

        def backtrack(start):

            if len(intermediate) == k:
                res.append(intermediate.copy())
                return

            for j in range(start, n+1):
                intermediate.append(j)
                backtrack(j + 1)
                intermediate.pop()

        backtrack(1)
        return res
