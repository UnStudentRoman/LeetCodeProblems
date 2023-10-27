class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        max_len = len(nums1) + len(nums2)
        last_val_nums1 = None
        i = 0
        j = 0
        while i + j < max_len//2:
            if nums1[i] > nums2[j]:
                i += 1
                last_val_nums1 = True
            else:
                j += 1
                last_val_nums1 = False
        print(i, j)
        if max_len % 2 == 1:
            if last_val_nums1:
                return nums1[i-j-1]
            else:

                return nums2[j-i-1]
        # elif max_len % 2 == 0:
        #     if last_val_nums1:
        #          if nums1[i+1] > nums2[j]:
        #              return nums1[i]
        #         return nums1[i]
        #     else:
        #         return nums2[j]
            # return 1000000000.000000


if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]

    obj = Solution()
    print(obj.findMedianSortedArrays(nums1,nums2))