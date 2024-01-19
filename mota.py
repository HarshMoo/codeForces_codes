def merge_and_sort(arr1,arr2):

    i = 0
    j = 0

    ans = []

    while i<len(arr1) and j<len(arr2):

        if(arr1[i]<arr2[j]):
            ans.append(arr1[i])
            i+=1

        else:
            ans.append(arr2[j])
            j+=1

    ans.extend(arr1[i:])
    ans.extend(arr2[j:])

    return ans

def merge_sort(arr):

    mid = len(arr)//2

    left = arr[mid:]
    right = arr[:mid]

    if(len(arr) == 1):
        return arr
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_and_sort(left,right)

arr = [5,6,8,2,3]

print(merge_sort(arr))