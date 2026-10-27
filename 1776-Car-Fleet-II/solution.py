class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # zip the two arrays together so it is easier to sort
        cars = list(zip(speed, position))
        stack = []

        for s, p in cars:

            time_to_reach = ( target - p ) / s
            
            if not stack:
                stack.append(time_to_reach)
                continue

            if len(stack) >= 1 and stack[-1] > time_to_reach:
                stack.append(time_to_reach)
            else:
                stack.pop()

        return len(stack)