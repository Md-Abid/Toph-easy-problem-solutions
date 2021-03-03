N=int(input())
di=[ ]
i=1
while N>0:
	if N%i==0:
		di.append(i)
	i+=1
	if i==N:
		break

print(len(di))
