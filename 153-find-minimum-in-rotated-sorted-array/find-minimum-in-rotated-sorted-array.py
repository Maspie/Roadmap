class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums) O(n) solution since it goes through array once, we need log n
        # log n's 20 times is 1 million for n

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
 
            else:
                r = mid
        return nums[l] 