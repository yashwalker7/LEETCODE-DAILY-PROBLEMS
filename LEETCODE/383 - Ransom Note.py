class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m=list(magazine)
        for i in ransomNote:
            if i in m:
                m.remove(i)
            else:
                return False
        return True