class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2) :
            nums1 , nums2 = nums2 , nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = len(nums1)

        while left <= right :

            i = (left+right) // 2
            j = (m+n+1)//2 - i

            leftA = float('-inf') if i == 0 else nums1[i-1]
            leftB = float('-inf') if j == 0 else nums2[j-1]

            rightA = float('inf') if i == m else nums1[i]
            rightB = float('inf') if j == n else nums2[j]

            if leftB <= rightA and leftA <= rightB :

                if (m+n)%2 != 0:
                    return max(leftA , leftB)

                return (max(leftA,leftB) + min(rightA , rightB)) / 2 

            elif leftA > rightB :
                right = i-1
            else:
                left = i+1 

        





        