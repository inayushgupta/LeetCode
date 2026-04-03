class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        c = len(matrix[0])
        r = len(matrix)

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        left, right = 0, r * c -1

        while left <= right:

            mid = left + (right - left) // 2
            row, col = mid//c, mid%c

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
               right = mid - 1
            else:
                left = mid + 1

        return False
