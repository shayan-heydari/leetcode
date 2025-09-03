class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fElement=strs[0]
        counter=0
        result[len(fElement)]=None
        for  i in range(len(fElement)):
            number=0
            for j in range(len(strs)):
                for x in range(len(strs[j])):
                    if fElement[i]==strs[j][x]:
                        number+=1
            result.append(number)
        return fElement[max(arr)]
            

        