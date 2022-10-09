class Solution(object):
    def singleNumber(self, nums):
        a = {}
        if (nums == [] ):
            return -1
        for d in nums:
            if (d in a):
                del a[d]
            else:
                a[d] = 1
        return list(a.keys())[0]
