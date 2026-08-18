class Solution:
    def isPalindrome(self, s: str) -> bool:
        ps=""
        for i in s:
            if i.isalnum():
                ps+=i.lower()
        left=0
        right=len(ps)-1
        while left<right:
            if ps[left]!=ps[right]:
                return False
            else:
                left+=1
                right-=1
        return True