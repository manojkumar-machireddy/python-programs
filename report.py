manoj = {} #Manoj marks storage subject wise
priya = {} #Priya marks storage subject wise
anup = {} # anup marks storage subject wise
#maths Marks 
manoj['maths'] =  24
priya['maths'] = 46
anup['maths'] =  60
# chemistry marks
manoj['chemistry'] =  44
priya['chemistry'] = 12
anup['chemistry'] =  13
# english marks
manoj['english'] =  55
priya['english'] = 66
anup['english'] =  69
# roll no
manoj['roll_no'] = 02
priya['roll_no'] = 04
anup['roll_no'] = 06
#computing total marks of each student
total_marks_manoj = manoj['maths'] + manoj['english'] + manoj['chemistry']
print ("The total marks obtained by manoj is", total_marks_manoj)
total_marks_priya = priya['maths'] + priya['english'] + priya['chemistry']
print ("The total marks obtained by priya is ", total_marks_priya)
total_marks_anup = anup['maths'] + anup['english'] + anup['chemistry']
print ("The total marks obtained by anup is ", total_marks_anup)
#Computing the maximum marks student
if ((total_marks_manoj > total_marks_anup) and (total_marks_manoj > total_marks_priya)):
	print ("Manoj got maximum_marks",total_marks_manoj,"his roll number is ", manoj['roll_no'])
elif ((total_marks_anup > total_marks_manoj) and (total_marks_anup > total_marks_priya)):
	print("Anup got maximum marks",total_marks_anup,"his roll no is", anup['roll_no'])
else:
	print ("Priya got maximum marks",total_marks_priya,"her roll no is ", priya['roll_no'])
