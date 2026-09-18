class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i!='C' and i!='D' and i!='+':
                stack.append(int(i))
            elif i=='D':
                val=stack[-1]*2
                stack.append(val)
            elif i=='C':
                stack.pop()
            elif i=='+':
                val1, val2= stack[-1], stack[-2]
                stack.append(val1+val2)
        return sum(stack)
    