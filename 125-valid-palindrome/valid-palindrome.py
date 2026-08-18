def checkLetter(n):
    return n.isalnum()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        for i in s:
            if checkLetter(i):
                lst.append(i.lower())
        left=0
        right=len(lst)-1
        while left<right:
            if lst[left]==lst[right]:
                left+=1
                right-=1
            else:
                return False
        return True