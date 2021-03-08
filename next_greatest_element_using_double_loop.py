def nge(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                print(arr[i], '--->', arr[j])
                flag = 1
                break 
        if flag == 0:
            print(arr[i], '---> -1')

arr = [11,13,21,3]
nge(arr)