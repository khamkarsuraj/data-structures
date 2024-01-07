# Insertion Sort
# Time: O(n^2)
# Space: O(1)

# For every ith element, find it's right position
# and place it there. Once found right position
# for ith element move to right side.
def main(arr):
    i = 0
    while i < len(arr):
        j = i - 1
        while j>=0 and arr[j]>arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
            i -= 1

        i += 1

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    main(arr)
    print(arr)