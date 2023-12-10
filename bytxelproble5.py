"""
You are given N number of books. Every ith book has Ai number of pages.


You have to allocate books to M number of students. There can be many ways or permutations to do so. In each permutation, one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations and print this minimum value. Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

A

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Sample Input format:

The first line consists of N number of books The second line consist of array element i.e. number of pages in a book.
the Third line consist of no. of students.

"""



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
