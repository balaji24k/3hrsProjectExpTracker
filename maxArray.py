arr = [5,-1,2,6,9,7]
arr.append(12)
max = arr[0]

for i in range (0,len(arr)):
    if max<arr[i]:
        max=arr[i]
        
print(max)
print(arr)
  
