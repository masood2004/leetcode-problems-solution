class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_list = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_list.append(nums[i])

        for i in range(len(new_list)):
            nums[i] = new_list[i]

        return len(new_list)
