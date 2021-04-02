'''
You can get the description of this searching here - https://www.geeksforgeeks.org/interpolation-search/
'''

def formula(high, low, element, arr):
    output = low + (element - arr[low]) * (high - low) / (arr[high] - arr[low])
    return int(output)

arr = [10, 20, 30]
element = 40
low = 0
high = len(arr) - 1
pos = formula(high, low, element, arr)
flag = 0

while low <= high and pos < len(arr):
    try:
        if arr[pos] == element:
            flag = 1
            break
        elif element > arr[pos]:
            low = pos + 1
        else:
            high = pos - 1
        pos = formula(high, low, element, arr)
    except:
        pass    

if flag == 0:
    print('Element not found!')
else:
    print('Element found at index',pos)        