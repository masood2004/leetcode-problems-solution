class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = list(map(str, s.split()))
        count = len(temp[-1])

        return count
