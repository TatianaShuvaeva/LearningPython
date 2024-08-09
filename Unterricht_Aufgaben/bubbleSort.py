def bubble_sort(a: list[int]) -> list[int]:
    
    n=len(a)
    for i in range (0,n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
    return a

# a = [2,9,6,3,2,1]
# sort_a = bubbleSort(a)
# print(sort_a)

# a = [12,-9,-6,33,2,1]
# sort_a = bubbleSort(a)
# print(sort_a)


assert bubble_sort([12,-9,-6,33,2,1]) == [-9, -6, 1, 2, 12, 33]
assert bubble_sort([2,9,6,3,2,1]) == [1, 2, 2, 3, 6, 9]
assert bubble_sort([1,0,-1]) == [-1, 0, 1]
assert bubble_sort([]) == []
assert bubble_sort([2]) == [2]

# https://www.sortvisualizer.com/bubblesort/ 