matrix = []
rows = int(raw_input("enter the number of rows:"))
for i in range(rows):
	matrix.append([])
columns = int(raw_input("enter the number of columns:"))
for j in range(rows):
	for k in range(columns):
		load = int(raw_input("enter the value:"))
		matrix[j].append(load)
print (matrix)
determinant = (matrix[0][0]*matrix[1][1]) - (matrix[1][0]*matrix[0][1])
print (int(determinant))
