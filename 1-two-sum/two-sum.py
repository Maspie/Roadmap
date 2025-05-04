class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = set()
        for i, num in enumerate(nums):

            if (target - num) in check:
                return (nums.index(target-num), i)

            check.add(num)
            

        