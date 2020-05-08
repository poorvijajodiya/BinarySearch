def BINARY_SEARCH(a,start,end,x):
	if end>=start:
		mid = int((start+end)/2)
		if a[mid] == x:
			return mid
		if a[mid]>x:
			return BINARY_SEARCH(a,start,mid-1,x)
		if a[mid]<x:
			return BINARY_SEARCH(a,mid+1,end,x)
	else:
		return -1
arr = sorted(['10','14','18','3','2','1','6','9','12','11','54','23','51','67','62','13','17'])
print(arr)
x = input("enter the number x you want to search : ")
result = BINARY_SEARCH(arr,0,len(arr)-1,x)
if result != -1:
	print("element is present at index {}".format(result))
else:
	print("element not found")
