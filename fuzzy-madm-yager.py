"""
Fuzzy MADM Yager Implementation in Python
Created by: RidwanBejo
"""

import math

# sample data
print "\ninitialization...."
sample_data = [
				[0.7, 0.5, 0.4],
				[0.3, 0.8, 0.6],
				[0.2, 0.3, 0.8],
				[0.5, 0.1, 0.2]
			]

saaty_matrix = [
				[1.0, 3.0, 7.0, 9.0],
				[1.0/3.0, 1.0, 6.0, 7.0],
				[1.0/7.0, 1.0/6.0, 1.0, 3.0],
				[1.0/9.0, 1.0/7.0, 1.0/3.0, 1.0]
			]

# weight vector processing
print "\ncreating weight_vector...."

vertical_result = []
for row in range(len(saaty_matrix)):
	temp_result = 0.0
	for col in range(len(saaty_matrix[0])):
		temp_result = temp_result + saaty_matrix[col][row]
	vertical_result.append(temp_result)

print vertical_result

weight_vector = []
for row in range(len(saaty_matrix)):
	temp_result = 0.0
	for col in range(len(saaty_matrix[0])):
		temp_result = temp_result + (saaty_matrix[row][col] / vertical_result[col])

	weight_vector.append(temp_result)

print weight_vector

# weighten the sample data

print "\nprocessing the sample data...."
weight_result = []
for row in range(len(sample_data)):
	temp_result = []
	for col in range(len(sample_data[0])):
		temp_result.append(math.pow(sample_data[row][col], weight_vector[row]))
	weight_result.append(temp_result)

print weight_result

d_value = []
for row in range(len(weight_result[0])):
	temp_d = []
	for col in range(len(weight_result)):
		temp_d.append(weight_result[col][row])

	d_value.append(min(temp_d))


# choose the candidate
print "\nchoosing the candidate...."
print d_value
print "result: ", max(d_value)