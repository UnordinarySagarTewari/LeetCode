class Solution:
    def countValidWords(self, sentence: str) -> int:
        def noDigits(s):
            for i in s:
                if 0<=ord(i)-ord('0')<=9:
                    return False
            return True
        def oneHyphen(s):
            count=0
            for i in range(len(s)):
                if count>1:
                    return False
                if s[i]=="-":
                    if (i==0 or i+1==len(s)):
                        return False
                    else:
                        count+=1
                        if 'a'<=s[i-1]<="z" and 'a'<=s[i+1]<="z":
                            pass
                        else:
                            return False
            if count<=1:
                return True
        def onePunctuation(s):
            for i in range(len(s)):
                if s[i] in ['.',',','!']:
                    if i!=len(s)-1:
                        return False
                    return True
            return True
        ans=0
        words = [i for i in sentence.split(" ") if len(i)!=0]
        for word in words:
            if noDigits(word) and oneHyphen(word) and onePunctuation(word):
                ans+=1
        return ans
