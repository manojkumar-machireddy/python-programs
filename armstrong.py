num = 371
ref = num
load = []
while (num != 0):
	load.append(num%10)
	num = num / 10
print (load)
value = 0
for j in load:
	value = j**3 + value

expr = value
if (expr == ref):
	print ("this is armstrong number ")
else:
	print ("not armstrong")

