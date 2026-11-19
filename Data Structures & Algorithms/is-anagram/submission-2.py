class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):

            for element in s : 
                if s.count(element)!= t.count(element):
                    return False
            return True
        else :
            return False
