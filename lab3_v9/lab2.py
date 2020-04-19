import os
import re
import sys
import math

def lab2_main():

	# Переменные
	table = []
	table_1 = []
	mbit_rate = 0.5
	kbit_free_total = 1000
	byte_total = bill_total = mbit_total = 0
	ip_client = '192.168.250.3'

	file_in = open('nfcapd202002251200.txt', 'r')

	[table_1.append(string.rstrip()) for string in file_in]

	for i in range(len(table_1)):
		table_1[i] = re.sub(r'\.\d\sM', '500000', table_1[i])

	[table.append(re.sub(r'\s+', ' ', elem).split(' ')) for elem in table_1[1:-4]]
	[row.remove('->') for row in table]
	[row.remove('->') for row in table]

	for row in table:
		if ip_client in row[5]:
			byte_total += int(row[9])

	mbit_total = math.ceil((byte_total*8 - kbit_free_total*1024)/(1024*1024))

	return ip_client, mbit_total, mbit_rate