# this code is trying to find the minimum coins required for going from city A to city B. The question is that one can go to the closest city from it by giving 1 coin  else go from city[x] to city[y] by giving |city[x]-city[y]| coins.

def mod(x):

    if(x>0):
        return x
    
    return -x

done = {}

def ek_ek(arr,start,end,coins):

    # this recursively calculates the number of coins required to go from city[a] to city [b] if going one by one. 

    if(start in done):
        return -1

    done[start] = 1

    ind1 = -1
    ind2 = -1

    for i in range(0,len(arr)):
        if(arr[i] == start):
            ind1 = i

        if(arr[i] == end):
            ind2 = i

    if(ind1 == ind2):
        return coins
    
    if(ind1 == 0 or ind1 == len(arr)-1):
        if(ind1 == 0):
            return ek_ek(arr,arr[ind1+1],end,coins+1)
        
        else:
            return ek_ek(arr,arr[ind1-1],end,coins+1)

    if(mod(arr[ind1+1]-arr[ind1])>mod(arr[ind1-1]-arr[ind1])):
        return ek_ek(arr,arr[ind1-1],end,coins+1)
    
    else:
        return ek_ek(arr,arr[ind1+1],end,coins+1)

def difference(arr,start,end):

    # this just calculates |city[a]-city[b]|

    return mod(end-start)

def main(arr,start,end):

    # this is the main function. Here code runs all functions come together to give out an answer

    start = arr[start-1]
    end = arr[end-1]

    value = ek_ek(arr,start,end,0)

    if(value == -1):
        return difference(arr,start,end)
    
    else:
        return min(difference(arr,start,end),value)


# test case
# cities5 = [7, 15, 20, 10, 25, 30, 5]
# start_city5_ind = 1
# end_city5_ind = 2
# print(main(cities5, start_city5_ind, end_city5_ind)) 
    
# output = 1