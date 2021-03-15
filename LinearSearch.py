# Program to implement linear search in a given array/list

def linearSearch(arr,search_item):
    print(f"search_item: {search_item}")  

    for i in arr:
        if (i == search_item):
            return -2,i        
            
    #print(f"i: {i}")
    return -1,-1
                


arr = [1,2,3,4,5]
search_item = 4
ans,position = linearSearch(arr, search_item)
#print(f"ans: {ans}") 
if ans == -1:
    print("Item not in array")
elif ans == -2:
    print(f"Item is in array at position: {position}")   
