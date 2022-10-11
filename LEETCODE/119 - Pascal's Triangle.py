class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        else:
            a = []
            a.append(1)
            for i in range(1, rowIndex+1):
                b = []
                b.append(1)
                for j in range(0, len(a) - 1):
                    b.append(a[j]+a[j+1])
                b.append(1)
                a = b
