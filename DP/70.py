class Solution:
    def climbStairs(self, n: int) -> int:
        
        # base case
        # where there is only 1 step then the total number of ways is 1
        # where there are 2 steps in total then the total number of ways is 2.
        # 1 + 1, 2

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # number of ways to reach the top
        # one_step means the person is one step behind the top
        # similarly, two_step means the person is two steps behind the top
        one_step = 1
        two_step = 2

        # calculate the number of ways to reach the top when n >= 3
        # this is an optimized dp solution
        # where we only care about the last 2 steps to reach the goal

        for _ in range(n-2):
            temp = two_step
            two_step = one_step + two_step
            one_step = temp

        return two_step


