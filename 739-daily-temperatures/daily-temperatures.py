class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temp = temperatures
        res = [0] * len(temp)
        stk = []

        for i, n in enumerate(temp):

            while stk and n > stk[-1][0]:

                main, index = stk.pop()

                res[index] = i - index

            stk.append((n, i))

        return res            

            

