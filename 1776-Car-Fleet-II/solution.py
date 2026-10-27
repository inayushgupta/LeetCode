class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # zip the two arrays together so it is easier to sort
        cars = list(zip(speed, position))
        stack = []

        for s, p in cars:

            stack.append(( target - p ) / s)

            if len(stack) >= 2 and stack[-2] <= stack[-1]:
                stack.pop()
            
        return len(stack)