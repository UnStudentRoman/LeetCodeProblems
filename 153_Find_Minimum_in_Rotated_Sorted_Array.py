class Solution:
    def findMin(self, nums) -> int:
        l = 0
        r = len(nums) - 1
        mid = l + (r - l) // 2
        while l < r:
            if nums[mid] < nums[r] < nums[l]:
                r = mid
                mid = r // 2
            elif nums[r] < nums[l] < nums[mid]:
                l = mid
                mid = l + (r - l) // 2
            if r - l == 1:
                if nums[r] > nums[l]:
                    return nums[l]
                else:
                    return nums[r]
        return nums[mid]


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    obj = Solution()
    print(obj.findMin(nums))