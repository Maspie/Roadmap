class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height) - 1
        length = r  
        max_area = 0
        while l < r:

            
            loat = min(height[l], height[r])
            area = loat * length

            max_area = max(area, max_area)

            if height[l] <= loat:
                l += 1
                length -= 1
            
            if height[r] <= loat:
                r -= 1
                length -= 1

        return max_area