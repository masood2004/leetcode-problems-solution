class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            reverse = int(str(x)[::-1])
            print(x)
            print(reverse)
            if reverse == x:
                return True
            else:
                return False
        else:
            return False
