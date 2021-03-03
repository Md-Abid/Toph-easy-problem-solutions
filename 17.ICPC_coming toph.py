s=input()
lst=[]
for charecter in s:
    lst.append(charecter)
    
print(max(lst ,key=lst.count))
