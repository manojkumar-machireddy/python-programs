active = True
while active:
	electricity_bill = int(raw_input("enter your reading:"))
	if (electricity_bill <= 100):
		charge = electricity_bill * 2.30
		print (int(charge))
	elif (electricity_bill > 100 and electricity_bill <= 400):
		new_bill = electricity_bill - 100
		charge = 230 + (new_bill*2.70)
		print (int(charge))
	elif (electricity_bill > 1000):
		new_bill = electricity_bill - 400
		charge = 1040 + (new_bill * 6)
		print (int(charge))
	message = raw_input("want to check for another reading,YES OR NO: ")
	if (message == "YES"):
		continue
	else:
		active =False
