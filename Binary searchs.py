
   #Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
result = binary_search(my_list, 23)
print(f"Element found at index: {result}")