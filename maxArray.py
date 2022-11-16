arr = [5,-1,2,6,9,7]
arr.append(12)
min = arr[0]
max = arr[0]

for i in range (0,len(arr)):
    if max < arr[i]:
        max = arr[i]
        
    if min > arr[i]:
        min = arr[i]
        
        
print("maximum:",max)
print("minimum:",min)
  
