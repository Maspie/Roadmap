class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        

        res = 0
        l = 0
        r = n-1
        max_right = height[r]
        max_left = height[l]
        while l < r:

            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left- height[l]

            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        

        return res




        


            
