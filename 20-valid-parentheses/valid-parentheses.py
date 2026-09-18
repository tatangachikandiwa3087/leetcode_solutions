class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        open_b='([{'#round, square, curly
        close_b=')]}'#round, square, curly
        for i in s:
            #open brackets go into the stack
            if i in open_b:#if stack is empty, sequence is invalid
                arr.append(i)
            else:#when close bracket is encountered
                if not arr:#if the stack is empty, sequence is invalid
                    return False
                else: 
                    #check if stack top is the corresponding bracket for this closing bracket
                    if i==')'  and arr[-1]=='(' or i==']'  and arr[-1]=='[' or i=='}'  and arr[-1]=='{':
                        arr.pop()
                    else:
                        return False
        return not arr
