class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maxcount=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:#same characters
                count+=1
            else:
                maxcount=max(count, maxcount)#update the max value
                count=1#set the count back to 1
        return max(count, maxcount)
