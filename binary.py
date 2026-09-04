def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
     return -1

arr=[1,3,5,7,8,9,11,13,15]
target=11

result=binary_search(arr,target)

if result!=-1:
   print("elements found at index:",result)
else:
    print("elements not found")