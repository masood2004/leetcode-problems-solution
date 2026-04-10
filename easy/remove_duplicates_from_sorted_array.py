
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

nums.sort()

new_list = []

for i in range(len(nums)):
    if (nums[i] != nums[i-1]):
        new_list.append(nums[i])
count = len(new_list)

# for i in range(len(nums) - len(new_list)):
#     new_list.append('_')

print(count, new_list, len(new_list))


# ================================================

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        new_list = []

        for i in range(len(nums)):
            if (nums[i] != nums[i-1]):
                new_list.append(nums[i])
        count = len(new_list)

        # for i in range(len(nums) - len(new_list)):
        #     new_list.append('_')

        # # int_type_list = [int(item) for item in new_list]

        return count
