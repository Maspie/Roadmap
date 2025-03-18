import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix = np.array(matrix)
        flatten = matrix.flatten()
        
        low  = 0
        high = len(flatten) - 1

        while low <= high:
            mid = (low + high) // 2

            if flatten[mid] == target:
                return True
            elif flatten[mid] > target:
                high = mid - 1

            else:
                low = mid + 1
        return False