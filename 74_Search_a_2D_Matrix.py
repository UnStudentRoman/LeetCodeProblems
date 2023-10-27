class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        i = 0
        while i < len(matrix):
            if target <= matrix[i][-1]:
                left = 0
                right = len(matrix[i])
                while left <= right:
                    middle = left + (right - left) // 2
                    if target > matrix[i][middle]:
                        left = middle + 1

                    elif target < matrix[i][middle]:
                        right = middle - 1

                    else:
                        return True
                return False
            i += 1


if __name__ == '__main__':
    nums = [[1]]
    target = 1

    obj = Solution()
    print(obj.searchMatrix(nums, target))