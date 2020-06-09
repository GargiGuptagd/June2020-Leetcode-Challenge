class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new=list(map(str,s))
        origin=list(map(str,t))
        count=0
        for i in new:
            if i in origin:
                count+=1
                origin=origin[origin.index(i)+1:]
                if origin==[]:
                    if count==len(new):
                        return True
                    else:
                        return False
            else:
                return False
        return True
                    