class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # we need to use backtracking
        subset = []
        def dfs(i): #i is the index here

            if i == len(nums):
                res.append(subset.copy())
                return


            #Decision to include
            subset.append(nums[i])
            dfs(i+1)

            #Decision to not include
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

        