class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
           sm=0
           while num!=0:
              rem=num%10
              sm+=rem
              num//=10
           num=sm
        return num
        



        