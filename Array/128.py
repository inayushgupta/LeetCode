class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        nums = set(nums)

        for n in nums:
            if n-1 not in nums:
                number = n
                length = 0
                while number in nums:
                    length += 1
                    number += 1
                longest = max(longest, length)

        return longest
