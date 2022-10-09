class Solution(object):
    def majorityElement(self, nums):
        a, count = 0,0
        for num in nums:
            if count == 0:
                a = num
                count += 1
            elif num == a:
                count += 1
            else:
                count -= 1
        return a
