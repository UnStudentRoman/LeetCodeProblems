class Solution:
    def twoSum(self, numbers, target: int):
        l = 0
        r = len(numbers) - 1
        repeating_nums = {}
        while l < r:
            if numbers[l] in repeating_nums:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
                numbers.pop()
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            else:
                l += 1

if __name__ == '__main__':
    numbers = [5,25,75]
    target = 100

    obj = Solution()
    print(obj.twoSum(numbers, target))