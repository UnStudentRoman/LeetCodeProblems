class Solution:

    def search(self, nums, target):
        if not nums or target < nums[0] or target > nums[-1]:
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

    def searchRange(self, nums, target):
        target_pos = self.search(nums, target)
        if target_pos == -1:
            return [-1, -1]
        else:
            l = target_pos - 1
            r = target_pos + 1
            if l < 0:
                pass
            else:
                while l >= 0 and nums[l] == nums[target_pos]:
                    l -= 1

            if r > len(nums):
                pass
            else:
                while r < len(nums) and nums[r] == nums[target_pos]:
                    r += 1
        return [l + 1, r - 1]


if __name__ == '__main__':
    nums = [1,4]
    target = 4

    obj = Solution()
    print(obj.searchRange(nums, target))
