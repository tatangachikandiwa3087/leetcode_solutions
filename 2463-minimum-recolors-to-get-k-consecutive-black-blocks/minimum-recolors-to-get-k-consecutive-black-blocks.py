class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        first_window=blocks[:k]
        w_c=0
        for i in first_window:
            if i=='W':
                w_c+=1
        mn=w_c
        for i in range(k,len(blocks)):
            if blocks[i]=="W":
                w_c+=1
            if blocks[i-k]=="W":
                w_c-=1
            mn=min(w_c,mn)
        return mn 
