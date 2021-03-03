hour,min=map(int,input().split())
hrangle=hour*30+min*(30/60)
minangle=min*6
result=0.0000000
if hrangle>minangle:
	result=hrangle-minangle
else:
	result=minangle-hrangle
if result>180:
	print(360-result)
else:
	print(result)