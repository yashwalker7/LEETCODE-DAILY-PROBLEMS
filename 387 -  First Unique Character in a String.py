class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=len(s)
        char=[0]*256
        
        for i in s:
            char[ord(i)]+=1
        
        idx=-1
        k=0
        
        for i in  s:
            if char[ord(i)]==1:
                idx=k
                break
            k+=1
        return idx