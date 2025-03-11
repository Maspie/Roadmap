class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        def backtrack(openC, closeC):

            # first we wanna have openC > n for appending the res
            # second we want to have openC > closeC

            if openC < n:

                stack.append("(")
                backtrack(openC+1, closeC)
                stack.pop()

            if openC > closeC:

                stack.append(")")
                backtrack(openC, closeC+1)
                stack.pop()

            if openC == n and closeC == n:
                res.append("".join(stack))

        backtrack(0,0)
        return res
            


            
            
            
            

            