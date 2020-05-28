# 快速排序：D&C（分而治之）,递归，归纳法，调用栈

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

array = [10, 5, 2, 3]
print(quicksort(array))
