class Solution(object):
    def matrixReshape(self, nums, r, c):
    
        row = len(nums)
        col = len(nums[0])
        result = [[0]*c for _ in range(r)]
        count = 0
        if row * col != 0 and row * col == r*c:
            rows = 0
            cols = 0
            for i in range(row):
                for j in range(col):
                    result[rows][cols] = nums[i][j]
                    cols += 1
                    if cols==c:
                        rows += 1
                        cols = 0
            return result
                
        else:
            return nums