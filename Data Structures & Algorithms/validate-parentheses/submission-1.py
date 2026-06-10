class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ope={'(':')','{':'}','[':']'}
        clo={')','}',']'}
        for i in s:
            if(i in ope):
                stack.append(i)
                continue
            else:
                if(len(stack)==0):
                    return False
                char=stack.pop()
                if(ope[char]!=i):
                    return False
        if(len(stack)>0):
            return False
        return True

        