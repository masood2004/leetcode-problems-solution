class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_in_base_10 = 0
        a_reversed = a[::-1]
        for i in range(len(a_reversed)):
            if a_reversed[i] == "1":
                a_in_base_10 += 2**i

        b_in_base_10 = 0
        b_reversed = b[::-1]
        for i in range(len(b_reversed)):
            if b_reversed[i] == "1":
                b_in_base_10 += 2**i

        sum_in_base_10 = a_in_base_10 + b_in_base_10

        if sum_in_base_10 == 0:
            return "0"

        res = ""
        while sum_in_base_10 > 0:
            res += str(sum_in_base_10 % 2)
            sum_in_base_10 //= 2

        return res[::-1]
