'''
 Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.

    1. The amount of petrol that every petrol pump has.
    2. Distance from that petrol pump to the next petrol pump.

 Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol
 pump and it has infinite capacity). Expected time complexity is O(n). Assume for 1-litre petrol, the truck can go 1 unit 
 of distance.

 For example, let there be 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as
 {4, 6}, {6, 5}, {7, 3} and {4, 5}. The first point from where the truck can make a circular tour is 2nd petrol pump. 
 Output should be “start = 1” (index of 2nd petrol pump).

 Time complexity = O(n^2)
'''

petrol = [6,7,4,10,6,5]
distance = [5,6,7,8,6,4]

size = len(petrol)

i = 0
while i < size:
    point = 0
    pet = petrol[i]
    dis = distance[i]
    p = pet - dis 
    # if petrol - distance is negative then switch to next point
    if p < 0:
        i += 1
        continue
    else:
        point += 1
        j = i
        while point < size and j%size < size:
            p = p + petrol[(j+1)%size] - distance[(j+1)%size]
            if p < 0:
                break 
            else:
                j = (j+1)%size
                point += 1        
        if point == size:
            print('Position =', i+1)
            break
    i += 1     