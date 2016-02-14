"""
SES (Simple Exponential Smoothing)
created by: Ridwan Bejo
"""
import math

dataset = [
			200.0,
			135.0,
			195.0,
			197.5,
			310.0,
			175.0,
			155.0,
			130.0,
			220.0,
			277.0,
			235.0,
		]

# variabel yang diperlukan oleh simple exponential smoothing
alpha = 0.9
list_ses = []
error = []
error_kuadrat = []
sum_error_kuadrat = 0.0

# inisialisasi nilai peramalan dengan menambahkan nilai pertama dari dataset sebagai nilai peramalan pertama
list_ses.append(dataset[0])

# menghitung alpha * Yt + (1 - alpha )* Yt^
dataset_len = len(dataset)
for i in range(1, dataset_len):
	try:
		yt_plus_1 = (alpha * dataset[i]) + ((1 - alpha) * list_ses[i-1])
		list_ses.append(yt_plus_1)
		print dataset[i]
		print 'nilai ses: ', yt_plus_1
	except Exception:
		continue
	print "\n------"

print '\n'

# menghitung error
for i in range(len(list_ses)):
	try:
		temp_error = dataset[i+1] - list_ses[i]
		error.append(temp_error)
		error_kuadrat.append(temp_error**2)
	except Exception:
		continue

# menghitung root mean squared error
mse = sum(error_kuadrat) / (len(list_ses) - 1)
print "mse: ", mse
print "perkiraan periode selanjutnya: ", list_ses[len(list_ses)-1]