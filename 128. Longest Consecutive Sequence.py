

def longestConsecutive(nums):
    nums = list(set(nums))
    nums.sort()
    i = 0
    result = 0
    intermediary_restul = 0
    while i < len(nums) - 1:
        if nums[i] + 1 == nums[i + 1]:
            intermediary_restul += 1
        elif result <= intermediary_restul:
            result = intermediary_restul
            intermediary_restul = 0
        else:
            intermediary_restul = 0
        i += 1
    if result < intermediary_restul:
        return intermediary_restul + 1
    return result + 1

if __name__ == '__main__':
    nums = [7,-9,3,-6,3,5,3,6,-2,-5,8,6,-4,-6,-4,-4,5,-9,2,7,0,0]

    print(longestConsecutive(nums))