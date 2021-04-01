arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
search_element = 110
flag = 0

for i, val in enumerate(arr):
    if search_element == val:
        flag = 1
        break 

if flag == 0:
    print('Element not found!')
else:
    print('Element found at index no.',i)    