class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m=len(name)
        n=len(typed)
        if n<m:
            return False
        i,j=0,0
        while(i<m and j<n):
            nameChar = name[i]
            typedChar = typed[j]
            if nameChar!=typedChar:
                print("nameChar!=typedChar")
                return False
            nameIndex = i+1
            typedIndex = j+1
            while(nameIndex<m and name[nameIndex]==nameChar):
                nameIndex+=1
            while(typedIndex<n and typed[typedIndex]==typedChar):
                typedIndex+=1
            if typedIndex-j < nameIndex-i:
                print("typedIndex-j < nameIndex-i")
                return False
            i=nameIndex
            j=typedIndex
        return i>=m and j>=n
