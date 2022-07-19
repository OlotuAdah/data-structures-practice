# takes in sorted array and a search key
# initiate left pointer as first item, right last item, m len divides by 2
# divides the array into two
import math


def binary_search(data, target, low, high):
    if low > high:
        return "Not found!"
    mid = (low + high) // 2
    print(mid)
    if target == data[mid]:
        return True
    if target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 32, 45, 90]
    search_key = 8
    initial_low = 0
    initial_high = len(sorted_data) - 1
    # print(initial_high)
    print(binary_search(sorted_data, search_key, initial_low, initial_high))
