def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high]
   for j in range(low , high):
      if arr[j] <= pivot:
         
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )



def partitionlowPivot(arr,low,high):
	i = low+1
	j = high
	pivot = arr[low]
	while(i<=j):
		while(arr[i]<pivot and i<high):
			i = i+1
		while(arr[j]>pivot):
			j = j-1
		if(i<j):
			arr[i],arr[j] = arr[j],arr[i]
			i = i+1
			j = j-1
		else:
			i = i+1
	arr[low] = arr[j]
	arr[j] = pivot
	return j

def quickSort(arr,low,high):
   if low < high:
      
      pi = partitionlowPivot(arr,low,high)
     
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

 


n=int(input("how many number you want to enter:"))
l=[]
for i in range(n):
    l.append(int(input()))
n = len(l)
quickSort(l,0,n-1)
print ("Sorted array is:")
for i in range(n):
   print (l[i],end=" ")