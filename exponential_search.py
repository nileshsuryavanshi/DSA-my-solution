'''
    ### Exponential search ###
    Time complexity = O(logN)
    Space complexity --- O(1) for iterative BS
                    |
                    ---- O(logN) for recursive BS

    Video link to understand this : https://www.youtube.com/watch?v=BDVYtuWXgXE&ab_channel=TECHDOSE
    Applications:
        1. Useful for unbounded array
        2. It works better than binary search

    Note: It required sorted array.    

'''

def binary_search(arr, start, end, element):
    flag = 0
    mid = int((start + end)/2)
    while start <= end:
        if arr[mid] == element:
            flag = 1
            break
        elif element > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = int((start + end)/2)

    if flag == 0:
        print('Element not found!')
    else:
        print('Element found at index',mid)


arr = [2,5,8,10,12,14,15,16]
element = 15

if arr[0] == element:
    print('Element found at index 0')
else:
    i = 1
    # exponential increasing the index
    while i < len(arr) and arr[i] <= element:
        i = i*2
    # passing the indices between which we have to apply binary search    
    binary_search(arr, i/2, min(i, len(arr)-1), element)        