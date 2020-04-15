import os
import re
import math
import matplotlib.pyplot as plt

table = []
table_1 = []
mbit_rate = 0.5
kbit_free_total = 1000
byte_total = bill_total = 0
ip_client = '192.168.250.3'

# os.system("nfdump -r nfcapd.202002251200 >> nfcapd202002251200.txt")
file_in = open('nfcapd202002251200.txt', 'r')

[table_1.append(string.rstrip()) for string in file_in]

for i in range(len(table_1)):
	table_1[i] = re.sub(r'\.\d\sM', '500000', table_1[i])

[table.append(re.sub(r'\s+', ' ', elem).split(' ')) for elem in table_1[1:-4]]
[row.remove('->') for row in table]
[row.remove('->') for row in table]

X_unsort = []
[X_unsort.append(re.sub(r':\d{2}\.{1}\d{3}', '', row[1])) for row in table]
Y_unsort = []
[Y_unsort.append(int(row[9])) for row in table]

XY_unsort = zip(X_unsort,Y_unsort)
XY = sorted(XY_unsort, key=lambda tup: tup[0])
X = [XY[0] for XY in XY]
Y = [XY[1] for XY in XY]

for i in range(len(X)):
	if i == len(X)-1:
		break
	if X[i] == X[i+1]:
		Y[i] += Y[i+1]
		del X[i+1]
		del Y[i+1]
		i -= 1

for row in table:
	if ip_client in row[5]:
		byte_total += int(row[9])

bill_total = math.ceil((byte_total*8 - kbit_free_total*1024)/(1024*1024)) * mbit_rate

print ('Затраты абонента', ip_client, 'составляют:', bill_total, 'руб.')

fig, ax = plt.subplots()
ax.bar(X, Y)
plt.ylabel('Объем трафика (бит)')
plt.xlabel('Время (поминутно)')
plt.show()

os.system("pause")
sys.exit(0)