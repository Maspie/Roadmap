class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        #rob1, rob2, n ...
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
        