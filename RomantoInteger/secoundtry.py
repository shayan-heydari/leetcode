class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        digit=1

        if len(s)>0:
            match s[0]:
                case 'I' :
                    num =1
                    if s[1]=='V':
                        num=4
                        digit=2
                    elif s[1]=='X':
                        num=9
                        digit=2
                case 'V':
                    num =5    
                case 'X':
                    num=10
                    if s[1]=='L':
                        num=40
                        digit=2
                    elif s[1]=='C':
                        num=90
                        digit=2
                case 'L':
                    num=50
                case 'C':
                    num=100
                    if s[1]=='D':
                        num=400
                        digit=2
                    elif s[1]=='M':
                        num=900
                        digit=2
                case 'D':
                    num=500
                case 'M':
                    num=1000
            return num+self.romanToInt(s[digit::])
        else:
            return 0