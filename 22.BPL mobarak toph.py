test = int(input())
for i in range (test):
	b = input()
	total_ball = 0
	for i in b:
		if i != "W" and i != "N" and i!="D":
			total_ball += 1
			over = int(total_ball / 6)
			balls = total_ball - (6 * over)
	if 0 < over < 2:
 			print(over, "OVER", end=" ")
	elif over > 1:
			print(over, "OVERS", end=" ")
	if balls == 1:
			print(balls, "BALL", end=" ")
	elif balls > 1:
			print(balls, "BALLS", end=" ")
	print(end="\n")