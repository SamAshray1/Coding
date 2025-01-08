class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        diffnums1 = nums1Set.difference(nums2Set)
        diffnums2 = nums2Set.difference(nums1Set)


        output = []
        output.append(list(diffnums1))
        output.append(list(diffnums2))
        return output