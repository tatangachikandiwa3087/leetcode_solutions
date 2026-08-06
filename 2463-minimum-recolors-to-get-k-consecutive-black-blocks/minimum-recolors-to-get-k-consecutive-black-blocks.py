class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mn=10000
        n=len(blocks)
        for right in range(n-k+1):
            c=0
            for i in range(k):
                if blocks[right+i]=='W':
                   c+=1
            mn=min(mn,c)
        return min(c, mn)
