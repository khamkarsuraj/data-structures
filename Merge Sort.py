# Merge Sort
# Time Complexity: O(logn)
# Space Complexity: O(1)
def merge(arrA, arrB):
    # Declare array
    arrC = []
    a, b = 0, 0

    # sort and append till you finish small array
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            arrC.append(arrA[a])
            a += 1
        else:
            arrC.append(arrB[b])
            b += 1
    
    # if arrB was smaller then append remaining arrA elements
    if a < len(arrA):
        arrC.extend(arrA[a:])
    
    # if arrA was smaller then append remaining arrB elements
    if b < len(arrB):
        arrC.extend(arrB[b:])
    
    # return merged array
    return arrC

def fun(a):
    # recursion call till only one element is there
    # calculate left and right for divided array
    left = 0
    right = len(a)-1
    if left < right:
        mid = (left + right) // 2
        # return merged array
        return merge(fun(a[left:mid+1]), fun(a[mid+1:right+1]))
    
    # return only one element left
    return a

arr = [87, 38, 1, 27, 43, 10]
print(fun(arr))