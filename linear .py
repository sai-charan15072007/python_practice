def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
        return -1

    arr=[10,20,45,35,50,25]
    target=5
    result=linear_search(arr,target)

    if result!=-1:
       print("element found at index:",result)
    else:
        print("element not found")