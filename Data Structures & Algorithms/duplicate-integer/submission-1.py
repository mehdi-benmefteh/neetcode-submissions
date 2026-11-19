from collections import Counter 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = Counter(nums)
        for element in new :
            if new[element]>1 :
                return True 
        return False 




        