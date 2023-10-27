class Solution:
    def search(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1
        left = 0
        right = len(nums)
        while left <= right:
            middle = left + (right - left) // 2
            if target > nums[middle]:
                left = middle + 1

            elif target < nums[middle]:
                right = middle - 1

            else:
                return middle
        return -1



if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9

    obj = Solution()
    print(obj.search(nums, target))