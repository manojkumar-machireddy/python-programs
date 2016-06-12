message = "thiseis a sample message"
print len(message)

i = int(raw_input("enter the starting point ,where to begin extraction:"))
j = int(raw_input("enter the ending point ,where to stop extraction:"))
sliced_portion = message[i:j]
print (sliced_portion)

