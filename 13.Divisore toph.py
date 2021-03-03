n1=int(input( ))
di=[]
i=1
while n1>0:
	if n1%i==0:
		di.append(i)
	i+=1
	if i>n1:
		break
for item in di:
	print(item)