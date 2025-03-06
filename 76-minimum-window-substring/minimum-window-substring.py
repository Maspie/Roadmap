class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        

        count_t = Counter(t)
        
        l = 0   
        need = len(count_t)
        have = 0
        min_streak = float("inf")
        window = {}
        res = [-1, -1]
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while have == need:

                if (r-l+1) < min_streak:
                    min_streak = r-l+1
                    res = [l, r]

                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l+=1
        l, r = res
        return s[l: r+1] if min_streak != float("inf") else ""