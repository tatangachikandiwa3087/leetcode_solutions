class Solution:
    def interpret(self, command: str) -> str:
        result=[]
        for i in range(len(command)):
            if command[i]=='G':
               result.append(command[i])
            if command[i]=='(':
               if command[i+1]==')':
                    result.append('o')
               else:
                    result.append('al')
        return "".join(result)