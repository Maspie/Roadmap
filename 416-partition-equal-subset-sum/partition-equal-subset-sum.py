class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target = target//2

        check = {0}
        for n in nums:
            temp = set()
            for i in check:
                if i +n == target:
                    return True
                    
                temp.add(i+n)

            check.update(temp)
        return False

        


        