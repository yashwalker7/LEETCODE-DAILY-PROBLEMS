class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for a in nums1:
            if a in nums2:
                output.append(a)
                nums2.remove(a)
        return output