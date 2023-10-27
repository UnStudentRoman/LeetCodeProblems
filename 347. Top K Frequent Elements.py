

def topKFrequent(nums, k):
    result = []
    val_times_pair = []
    for val in set(nums):
        val_times_pair.append((nums.count(val), val))
    val_times_pair.sort(reverse=True)
    for i in range(k):
        result.append(val_times_pair[i][1])
    return result


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))
