class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        res = []
        temp = []
        for i,a in enumerate(nums):

            if i > 0 and a == (nums[i - 1]):
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                if (a + nums[l] + nums[r]) > 0:
                    r -= 1

                elif (a + nums[l] + nums[r]) < 0:
                    l += 1

                elif (a + nums[l] + nums[r]) == 0:
                    temp = [a, nums[l], nums[r]]
                    if temp not in res:
                        res.append(temp)
                    l+=1
                
            
            
        return res