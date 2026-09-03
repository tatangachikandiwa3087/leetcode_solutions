class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lst=list(haystack)
        lst1=list(needle)
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1