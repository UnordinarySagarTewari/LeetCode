class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif len(stack)>0:
                if abs(ord(stack[-1])-ord(i))==32:
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)
