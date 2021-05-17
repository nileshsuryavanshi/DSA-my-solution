'''
    ### Sliding Window Maximum (Maximum of all subarrays of size k)
        Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.

        Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
        Output: 3 3 4 5 5 5 6

        Explanation: 
        Maximum of 1, 2, 3 is 3
        Maximum of 2, 3, 1 is 3
        Maximum of 3, 1, 4 is 4
        Maximum of 1, 4, 5 is 5
        Maximum of 4, 5, 2 is 5 
        Maximum of 5, 2, 3 is 5
        Maximum of 2, 3, 6 is 6

    ### Time complexity --- O(n)    
'''

def windowMax(arr, k):
    # initially set first item to max
    max = arr[0]
    count = 0
    # iterate each item from array
    for element in arr:
        if max < element:
            max = element
        count += 1
        # print max when count >= k
        if count >= k:
            print(max, end=' ')
    print()

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
windowMax(arr, 3)            