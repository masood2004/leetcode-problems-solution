class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        two_steps_together = 1
        one_step_only = 2

        for i in range(3, n+1):
            current_step = one_step_only + two_steps_together
            two_steps_together = one_step_only
            one_step_only = current_step

        return one_step_only
