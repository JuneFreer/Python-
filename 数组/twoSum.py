# 暴力求解


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    print('do not found such numbers!')

test_nums = [3, 5, 7, 4, 1]
test_target = 9

if __name__ == '__main__':
    print(twoSum(test_nums, test_target))
