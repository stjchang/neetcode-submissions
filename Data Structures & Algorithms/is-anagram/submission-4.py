class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        ''' instead of manually appending to list, you can just call sorted on string itself
        slist = []
        t_list = []

        for x in s:
            s_list.append(x)
        for y in t:
            t_list.append(y)
_
        if sorted(s_list) == sorted(t_list):
            return True
        return False ''' 

        
        
                
        