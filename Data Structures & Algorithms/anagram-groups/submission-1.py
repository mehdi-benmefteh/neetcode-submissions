class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        for element in strs :
            e= "".join(sorted(element))
            if e in dic :
                dic[e].append(element)
            else :
                dic[e]=[element]


        return list(dic.values()) 

        