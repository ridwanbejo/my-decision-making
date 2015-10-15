"""
Weighted Product Implementation in Python
Created by: RidwanBejo
"""

import math

# sample data
print "\ninitialization...."
sample_data = [
				# [4, 4, 5, 3, 3],
				# [3, 3, 4, 2, 3],
				# [5, 4, 2, 2, 2],
				[0.75, 2000, 18, 50, 500],
				[0.50, 1500, 20, 40, 450],
				[0.90, 2050, 35, 35, 800],
			]

# choosen_weight
weight = [{'val':5, 'type':'cost'}, 
		{'val':3, 'type':'benefit'}, 
		{'val':4, 'type':'cost'}, 
		{'val':4, 'type':'benefit'}, 
		{'val':2, 'type':'cost'}]

# refined weight
total_weight = 0.0
for w in weight:
	total_weight = total_weight + w['val']

refined_weight = []
for w in weight:
	temp_weight = w['val'] / total_weight
	refined_weight.append(temp_weight)

print refined_weight

# matrix normalization
print "\n\nnormalize the matrix...."

normalize_matrix = []

for row in range(len(sample_data)):
	result_row_data = []
	for col in range(len(sample_data[0])):

		temp_refined_weight = refined_weight[col]
		
		if weight[col]['type'] == 'cost':
			temp_refined_weight = refined_weight[col] * -1.0

		temp_value = math.pow(sample_data[row][col], temp_refined_weight)
		result_row_data.append(temp_value)

	normalize_matrix.append(result_row_data)

print normalize_matrix

# create the vector
print "\n\nprocessing the weight vector...."

weight_vector = []
for row in range(len(normalize_matrix)):
	temp_result = 1.0
	for col in range(len(normalize_matrix[0])):
		temp_result = temp_result * normalize_matrix[row][col]	
	weight_vector.append(temp_result)

print weight_vector

# ranking process weight * normalize_matrix
print "\n\nprocessing the ranking...."

total_weight_vector = float(sum(weight_vector))

ranking_list = []
for row in weight_vector:
	candidate_rate = row / total_weight_vector
	ranking_list.append(candidate_rate)

print len(ranking_list)
print ranking_list

# get the chosen candidate
the_candidate = max(ranking_list)
print "\n\nThe candidate is: ", the_candidate