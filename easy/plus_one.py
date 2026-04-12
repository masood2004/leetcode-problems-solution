class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])

        result_num = str(int(num) + 1)

        result_str = [int(x) for x in result_num]

        return result_str
