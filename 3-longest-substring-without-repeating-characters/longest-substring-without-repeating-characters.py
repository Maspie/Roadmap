class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        check = set()
        max_streak = 0
        
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1

            check.add(s[r])
            max_streak = max(max_streak, r-l+1)

        return max_streak
