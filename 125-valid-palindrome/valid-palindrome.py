class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lis =[]
        s = s.lower()
        for char in s:
            if char.isalnum():
                lis.append(char)
        print(s)    
        l = 0
        r = len(lis) - 1
        while l < r:

            if lis[l] == lis[r]:
                l += 1
                r -= 1
                
            
            else:
                return False
            

        return True
