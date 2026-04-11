class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = [nums[0]]

        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                new_list.append(nums[i])

        for i in range(len(new_list)):
            nums[i] = new_list[i]

        return len(new_list)
