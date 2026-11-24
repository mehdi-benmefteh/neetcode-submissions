class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic =defaultdict(list)
        for e in strs :
          count = [0]*26
          for ee in e :
            count [ord("a")-ord(ee)]+=1
          dic[tuple(count)].append(e)


        return list(dic.values()) 

        