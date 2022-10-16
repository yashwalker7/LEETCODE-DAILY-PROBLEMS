class Solution:
    def minDifficulty(self, jobDifficulty: List[int], dayCount: int) -> int:
        jobCount = len(jobDifficulty)
        if jobCount < dayCount:
            return -1
        @functools.lru_cache(None)
        def topDown(jobIndex: int, remainDayCount: int) -> int:
            remainJobCount = jobCount - jobIndex
            if remainDayCount == 1:
                return max(jobDifficulty[jobIndex:])
            
            if remainJobCount == remainDayCount:
                return sum(jobDifficulty[jobIndex:])
            minDiff = float('inf')
            maxOfToday = 0
            for i in range(jobIndex, jobCount - remainDayCount + 1):
                maxOfToday = max(maxOfToday, jobDifficulty[i])
                minDiff = min(minDiff, maxOfToday + topDown(i+1, remainDayCount-1))
            return minDiff

        return topDown(0, dayCount)
