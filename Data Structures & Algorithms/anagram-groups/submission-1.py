class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortHash = {}
        retList =[]
        index = 0
        for st in strs:
            sortStr = ''.join(sorted(st))
            if sortStr not in sortHash:
                sortHash[sortStr] =index
                retList.append([st])
                index+=1
            else:
                i =sortHash[sortStr]
                retList[i].append(st)
        return retList
