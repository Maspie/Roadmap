import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        



        bot, top = 0, len(matrix) - 1

        while bot <= top:

            midrow = (bot + top) // 2

            if matrix[midrow][-1] < target:

                bot = midrow + 1

            elif matrix[midrow][0] > target:

                top = midrow - 1

            else:
                break
        if not (bot<= top):
            return False
            
        low, high = 0, len(matrix[midrow]) - 1


        while low <= high:
            mid = (low + high) // 2

            if matrix[midrow][mid] == target:
                return True
             
            elif matrix[midrow][mid] > target:
                high = mid - 1

            else:

                low = mid + 1
        return False










        # matrix = np.array(matrix)
        # flatten = matrix.flatten()
        
        # low  = 0
        # high = len(flatten) - 1

        # while low <= high:
        #     mid = (low + high) // 2

        #     if flatten[mid] == target:
        #         return True
        #     elif flatten[mid] > target:
        #         high = mid - 1

        #     else:
        #         low = mid + 1
        # return False