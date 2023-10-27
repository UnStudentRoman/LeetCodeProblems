
def prodCalc(nums):
    if not nums:
        return 1
    prod = 1
    for val in nums:
        prod *= val
    return prod

def productExceptSelf(nums):
    ref = {}
    result = []
    pointer = 0
    while pointer < len(nums):
        if nums[pointer] in ref.keys():
            result.append(ref[nums[pointer]])
        else:
            before = prodCalc(nums[:pointer])
            after = prodCalc(nums[pointer+1:])
            result.append(before*after)
            ref[nums[pointer]] = before*after
        pointer += 1
    return result




if __name__ == '__main__':
    nums = [-1,-1,1,0,-3,3,3]
    print(productExceptSelf(nums))
