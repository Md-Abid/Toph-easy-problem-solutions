n=int(input())
li=list(map(int,input().split())) [:n]
avg=0
v=1
for i in range(0,n):
	avg+=li[i]
	result=(avg/v)
	print(result)
	v+=1
	