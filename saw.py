"""
Simple Additive Weighthing Implementation in Python
Created by: RidwanBejo
"""

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


# matrix normalization
print "\n\nnormalize the matrix...."

normalize_matrix = []

for row in range(len(sample_data)):
	result_row_data = []
	for col in range(len(sample_data[0])):
		max_rate = []
		for x in range(len(sample_data)):
			max_rate.append(float(sample_data[x][col]))

		if weight[col]['type'] == 'cost':
			temp_result =  min(max_rate) / float(sample_data[row][col])
		elif weight[col]['type'] == 'benefit':
			temp_result = float(sample_data[row][col]) / max(max_rate)
		
		result_row_data.append(temp_result)

	normalize_matrix.append(result_row_data)

print normalize_matrix

# ranking process weight * normalize_matrix
print "\n\nprocessing the ranking...."

ranking_list = []
for row in range(len(normalize_matrix)):
	candidate_rate = 0.0
	for col in range(len(normalize_matrix[0])):
		# print normalize_matrix[row][col], weight[col]
		temp_result = normalize_matrix[row][col] * float(weight[col]['val'])	
		candidate_rate = candidate_rate + temp_result
	ranking_list.append(candidate_rate)

print len(ranking_list)
print ranking_list

# get the chosen candidate
the_candidate = max(ranking_list)
print "\n\nThe candidate is: ", the_candidate