arr = [2,5,8,10,12,14,15,16]
element = 2
start = 0
end = len(arr) - 1
mid = int((start + end)/2)
flag = 0

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