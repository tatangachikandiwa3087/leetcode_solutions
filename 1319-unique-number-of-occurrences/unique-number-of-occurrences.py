class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        lst=[]
        for i in arr:
            d[i]=d.get(i, 0)+1
        for i in d:
            lst.append(d[i])
        if len(lst)!=len(set(lst)):
            return False
        return True