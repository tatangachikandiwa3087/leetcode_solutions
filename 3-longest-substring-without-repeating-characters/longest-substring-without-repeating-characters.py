class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        left=0
        max_=0
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left+=1
            d.add(s[right])
            max_=max(max_, right-left+1)
        return max_


