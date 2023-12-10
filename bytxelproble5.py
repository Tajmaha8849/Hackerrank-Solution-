def Min_pages(n,nb,ns):
	arr1=[]
	arr2=[]
	lstmax=[]
	sum1,sum2=0,0
	for i in range(len(nb)-1):
		arr1.append(nb[i])
		for j in range(len(arr1)):
			sum1+=arr1[j]
		for k in range(i+1,len(nb)):
			arr2.append(nb[k])
		for m in range(len(arr2)):
			sum2=sum2+arr2[m]
		if(sum1>sum2):
			lstmax.append(sum1)
		else:
			lstmax.append(sum2)
		sum1,sum2=0,0
		arr2=[]
	return min(lstmax)
n=int(input()) #no of books
nb=[12,34,67,90]  #array of number of pages of books
ns=int(input()) #no of student
print(Min_pages(n,nb,ns))