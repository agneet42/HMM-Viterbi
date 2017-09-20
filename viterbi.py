import numpy as np
import csv
import math
import itertools

line = open("transitionMatrix.txt")
transitionMatrix_temp = []
temp = []

s = ""
space_count = 0
for i in line:
	i = i + " "
	i = i + " "
	for val in i:
		if(val==" " and space_count == 0):
			temp.append((s))
			space_count = space_count + 1
			s = ""
		elif(val==" " and space_count == 1):
			space_count = 0
		else:
			s = s + val
	transitionMatrix_temp.append(temp)
	temp = []

for i in transitionMatrix_temp:
	char = i[42]
	l = len(char)
	char = char[:l-1]
	i[42] = char

temp = []

transitionMatrix = []
for arr in transitionMatrix_temp:
	temp = list(map(float,arr))
	transitionMatrix.append(temp)
	temp = []

init_prob = csv.reader(open("InitialProbability.csv","r"))

init_arr = []
for lines in init_prob:
	init_arr.append([int(lines[0])-6,float(lines[1])])

# init_arr[0] == class label

observed_class_arr_temp = []
count = 0

observed_class = csv.reader(open("observedClass.csv","r"))

for i in observed_class:
	observed_class_arr_temp.append(i)
	count = len(i)

count_array = []
for j in range(0,count):
	count_array.append(j)

observed_class_arr = []
temp = []
for j in count_array:
	for val in observed_class_arr_temp:
		temp.append(int(val[j]))
	observed_class_arr.append(temp)
	temp = []

temp = []

observed_probability_arr_temp = []
count = 0

observed_probability = csv.reader(open("observedProbability.csv","r"))

for i in observed_probability:
	observed_probability_arr_temp.append(i)
	count = len(i)

count_array = []
for j in range(0,count):
	count_array.append(j)

observed_probability_arr = []
temp = []
for j in count_array:
	for val in observed_probability_arr_temp:
		temp.append(float(val[j]))
	observed_probability_arr.append(temp)
	temp = []

path_array = []
temp = []
value_array = []

# Initial
for i in range(0,5):
	path_array.append([observed_class_arr[0][i]])
	val = observed_class_arr[0][i] 
	val1 = init_arr[val-1][1]
	value_array.append([((val1) * (observed_probability_arr[0][i]))])

# 1 to 2

for i in range(0,len(observed_class_arr)):
	temp1 = np.asarray(path_array)
	temp2 = np.repeat(temp1,5,axis=0)
	path_array = temp2.tolist() 
	temp1 = np.asarray(value_array)
	temp2 = np.repeat(temp1,5,axis=0)
	value_array = temp2.tolist() 
	x = 0
	for k in range(0,5):
		val = observed_class_arr[i][k]
		for j in range(0,5):
			val1 = observed_class_arr[i+1][j]
			trans_temp = transitionMatrix[val-1][val1-1]
			val2 = observed_probability_arr[i+1][j]
			ans = trans_temp * val2
			path_array[x].append(val1)
			value_array[x][0] = value_array[x][0] * ans
			x = x + 1
	path_array = [path_array for (value_array,path_array) in sorted(zip(value_array,path_array),reverse=True,key=lambda pair: pair[0])]
	value_array.sort(key=lambda x: x[0],reverse=True)
	path_array = path_array[:5]
	value_array = value_array[:5]
	break

# Rest

for i in range(1,len(observed_class_arr)-1):
	temp1 = np.asarray(path_array)
	temp2 = np.repeat(temp1,5,axis=0)
	path_array = temp2.tolist() 
	temp1 = np.asarray(value_array)
	temp2 = np.repeat(temp1,5,axis=0)
	value_array = temp2.tolist() 
	temp_path = []
	temp_val = []
	for y in range(0,5):
		val = observed_class_arr[i][y]
		for x in range(0,5):
			val1 = observed_class_arr[i+1][x]
			trans_temp = transitionMatrix[val-1][val1-1]
			val2 = observed_probability_arr[i+1][x]
			ans = trans_temp * val2
			temp_path.append([val,val1])
			temp_val.append([ans])
	
	count = 0
	restore = []
	for y in range(0,len(path_array)):
		to_check = path_array[y][-1]
		for loop in range(0,len(temp_path)):
			to_check_1 = temp_path[loop][0]
			to_value_1 = temp_val[loop][0]
			if(to_check == to_check_1 and to_check_1 != -1):
				path_array[y].append(temp_path[loop][1])
				value_array[y][0] = value_array[y][0] * to_value_1
				restore.append(temp_path[loop][0])
				temp_path[loop][0] = -1
				count = count + 1
				break
		if(count==5):
			count = 0
			for a in restore:
				for arr in temp_path:
					if(arr[0] == -1):
						arr[0] = a
						break
			restore = [] 
	path_array = [path_array for (value_array,path_array) in sorted(zip(value_array,path_array),reverse=True,key=lambda pair: pair[0])]
	value_array.sort(key=lambda x: x[0],reverse=True)
	path_array = path_array[:5]
	value_array = value_array[:5]
	temp_path = []
	temp_val = []

for i in range(0,len(path_array)):
	print(path_array[i],value_array[i])
