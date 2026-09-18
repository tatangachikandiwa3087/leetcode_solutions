class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr=[]
        for i in s:
            if not arr:
                arr.append(i)
            else:
                if arr[-1]==i:
                    arr.pop()
                else:
                    arr.append(i)
        return "".join(arr)

