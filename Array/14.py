class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for i in range(1, len(strs)):

            string = strs[i]
            index = 0

            while index < len(prefix) and index < len(string):
                if not string[index] == prefix[index]:
                    break
                index += 1

            prefix = string[:index]
            
        return prefix

