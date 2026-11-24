from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res=[]
        for i in range (k) :
            key= max(freq, key=freq.get)
            res.append(key)
            del freq[key]



        return res