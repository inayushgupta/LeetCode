class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        mapping = {}
        used_t = set()
        
        for i in range(len(s)):

            s_char = s[i]
            t_char = t[i]

            if s_char in mapping:
                if t_char != mapping[s_char]:
                    return False
            else:
                if t_char in used_t:
                    return False
                else:
                    mapping[s_char] = t_char
                    used_t.add(t_char)
        return True
