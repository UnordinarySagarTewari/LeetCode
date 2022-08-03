class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            d={}
            for i in s:
                if i in d:
                    return True
                if i not in d:
                    d[i]=1
            return False
        else:
            arr=[]
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    arr.append(i)
            return len(arr)==2 and s[arr[0]]==goal[arr[1]] and s[arr[1]]==goal[arr[0]]
