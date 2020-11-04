num=int(input("Inter Number: "))
deff50=int()
if num ==0 or num == 160:
	print("Invalid")
if num in range(41):
	print(8*num)
if num > 40 and num <= 50:
	deff=num - 40
	print(40*8+deff*9)
if num > 50:
	deff40=num-40
	if deff40 > 10:
		deff50=deff40 - 10
		deff40=10
	print((40*8)+(deff50 * 10 )  + (deff40 * 9))
