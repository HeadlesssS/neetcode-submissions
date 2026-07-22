
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) ==1:
            return [strs]
        sortList=[]
        retList =[]
        for st in strs:
            sortStr = sorted(st)
            if sortStr not in sortList:
                sortList.append(sortStr)
                retList.append([st])
            else:
                i =sortList.index(sortStr)
                retList[i].append(st)

        return retList
