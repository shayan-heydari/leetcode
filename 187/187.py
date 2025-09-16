class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        resault=[]
        n=0
        sample =[None]*[10]
        for i in range(len(s)):
            value=True
            for j in range(i,i+10):
                sample[j]=s[j]
            for x in s:
                if sample[n]!=s[x]:
                    n=0
                    value=False
                elif  sample[x]==s[x] and sample[x+1]==None and value!=true :
                    for c in range (len(sample)):
                        resault.append(sample[c])
                n+=1
        return resault

