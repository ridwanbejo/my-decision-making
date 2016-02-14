import math

moving_average = 2
daftar_omzet = [
			131, 
			130, 
			125, 
			126, 
			129, 
			132, 
			130, 
			132, 
			139, 
			137, 
			137, 
			140, 
			143, 
			143, 
			141, 
			143, 
			148, 
			152, 
			152
		]

list_yt_plus_1 = []
error = []
error_kuadrat = []
sum_error_kuadrat = 0.0

# menghitung yt + 1
daftar_omzet_len = len(daftar_omzet)
for i in range(daftar_omzet_len):
	try:
		sum_ma = 0
		for j in range(moving_average):
			print daftar_omzet[i + j],' ',
			sum_ma = sum_ma + daftar_omzet[i + j]
		yt_plus_1 = sum_ma * 1.0 / moving_average
		print yt_plus_1
		list_yt_plus_1.append(round(yt_plus_1, 3))
	except Exception:
		continue
	print "\n------"

print '\n'	
print len(list_yt_plus_1)
print list_yt_plus_1

# menghitung error
for i in range(len(list_yt_plus_1)):
	try:
		error_i = daftar_omzet[i + moving_average] - list_yt_plus_1[i]
		error.append(round(error_i, 3))
		error_kuadrat.append(round(error_i ** 2, 3))
	except Exception:
		continue

sum_error_kuadrat = sum(error_kuadrat)

print error
print len(error_kuadrat)
print sum_error_kuadrat

# menghitung root mean squared error
rmse = math.sqrt( sum_error_kuadrat / len(error_kuadrat))
print "rmse: ", rmse