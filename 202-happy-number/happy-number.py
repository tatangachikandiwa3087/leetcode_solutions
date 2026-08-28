
def getdigitsum(n):
    dsum=0
    while n>0:
        r=n%10
        dsum+=r*r
        n//=10
    return dsum
class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            if n<10:
                break
            n=getdigitsum(n)
        if n==1 or n==7:
            return True
        else:
            return False