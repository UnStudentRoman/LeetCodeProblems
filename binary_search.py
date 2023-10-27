def binary_search(lst, target):
    left = 0
    right = len(lst)-1
    while left < right:
        mid = ((right + left) // 2)
        if target > lst[mid]:
            left = mid + 1
        elif target < lst[mid]:
            right = mid - 1
        elif target == lst[mid]:
            return mid
    return None



if __name__ == '__main__':
    lst = [i*2 for i in range(2147483648)]
    target = 31268
    print(binary_search(lst, target))

