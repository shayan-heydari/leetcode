class Solution(object):
    def isPalindrome(self, x):
        if type(x) == int:
            string = str(x)
        else:
            string = x  # keep as string in recursion

        if len(string) <= 1:
            return True
        if string[0] != string[-1]:
            return False
        return self.isPalindrome(string[1:-1])
