def binarySearch(arr, num):
    #print(f"{arr}")
    #l = 
    mid = (len(arr)/2) + 1
    mid = int(mid)
   # print(f"{mid}")
    if (num == arr[mid]):
        return True
    elif (num > arr[mid]):
        binarySearch(arr[mid:], num)
    elif (num < arr[mid]):
        binarySearch(arr[:mid-1], num)
    else:
        return False

lst = [1,2,3,4,5]
value = 1

Result = binarySearch(lst, value)
#binarySearch()

if (Result == True):
    print(f"Number found at position")
else:
    print(f"Number not in the array")

