# 创建一个哈希表

def twoSum(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table.get(complement), i]
        hash_table[nums[i]] = i

nums = [2, 5, 1, 6]
target = 8

if __name__ == "__main__":
    result = twoSum(nums, target)
    print(result)
