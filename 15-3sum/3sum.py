class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        res = []
        
        for i,a in enumerate(nums):

            if a > 0:
                break
            if i > 0 and a == (nums[i - 1]):
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                if (a + nums[l] + nums[r]) > 0:
                    r -= 1

                elif (a + nums[l] + nums[r]) < 0:
                    l += 1

                else:
                    
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                
                    while l < r and nums[l-1] == nums[l]:
                        l += 1

                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
            
        return res