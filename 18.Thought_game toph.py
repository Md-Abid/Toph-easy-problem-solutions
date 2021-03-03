test_cases = int(input())
d = []
for i in range(test_cases):
	a, b = map(int, input().split())
	c = (a + b) //2
	if c % 2 == 0:
		d.append("Sadia will be happy.")
	else:
		d.append("Oops!")
for i in d:
	print(i)