def partition(array, i, j):
    a = i - 1
    p = array[j]
  
    for k in range(i, j):
        if array[k] < p:
            a = a + 1
            array[a], array[k] = array[k], array[a]

    array[a+1], array[j] = array[j], array[a+1]
    return a+1
 
def quickSort(new_a, i, j): 
    if i < j:
        p = partition(new_a, i, j)
        quickSort(new_a, i, p-1)
        quickSort(new_a, p+1, j)

arr = [4,3,-1,5,2,9,10,0]
n = len(arr)-1
quickSort(arr, 0, n)
print(arr)