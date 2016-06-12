entries = [34,5,7,67,4,100,2]
active = True
while active:
#	values = int(raw_input("enter the values:"))
#	entries.append(values)
	message = raw_input("want to enter another value, Y OR N:")
	if (message == 'Y'):
		continue
	else: 
		active = False
print ("the current entries are", entries)
minimum = entries[0]
sorted_array = []
while entries:
	#minimum = entries[0]
	for i in entries:
		#print (i)
		if (i < minimum):
			minimum = i 
			#print (minimum)
	sorted_array.append(minimum)
	print entries
	print minimum
	entries.remove(minimum)
print (sorted_array)
	

