def Binary_search(arr, low, high, t):
    if low> high:
        return(-1)
    mid= (low+high)//2
    if arr[mid]== t:
        return(mid)
    elif mid < t:
        low=mid+1
    else:
        high= mid +1
        

    