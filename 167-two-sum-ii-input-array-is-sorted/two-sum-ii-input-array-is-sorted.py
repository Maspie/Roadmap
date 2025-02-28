class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(numbers) - 1

        while  l < r:

            

            while target - numbers[r] < numbers[l]:
                r -= 1

            while target - numbers[r] > numbers[l]:
                l += 1

            if target - numbers[r] == numbers[l]:
                return [l+1 , r+1]

        