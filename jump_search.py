'''
Suppose we have an array arr[] of size n and block (to be jumped) size m.
Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on.
Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search 
operation from the index km to find the element x.

    Time Complexity : O(√n) 
    Auxiliary Space : O(1)
'''

arr = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
element = 3
jump = 8
start = flag = 0
end = jump

if jump <= len(arr):
    while end < len(arr):
        # break if the element come in jump window otherwise go to next next jump
        if arr[start] <= element and  element <= arr[end]:
            break
        else:
            start = end 
            end = end + jump

    # if end index is more than the array size then assign last index to end        
    if end > len(arr) - 1:
        end = len(arr) - 1

    # applying linear search after getting the starting and ending index for the jump
    for i in range(start, end+1):
        if arr[i] == element:
            flag = 1
            break 

    if flag == 0:
        print('Element not found!')
    else:
        print('Element found at index',i)    

else:
    print('Jump should be less than or equal to array size!')        