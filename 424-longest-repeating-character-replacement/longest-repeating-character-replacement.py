class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        l = 0
        res = 0
        maxf = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            maxf = max(maxf, max(count.values()))

            while ((r-l+1) - maxf) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res