class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        new_list = [target]

        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            new_list.extend(nums)
            new_list.sort()
            for j in range(len(new_list)):
                if new_list[j] == target:
                    return j
