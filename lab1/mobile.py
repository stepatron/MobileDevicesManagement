import os

# Функция поиска записей о действиях абонента и подсчета стоимости услуг звонков и смс
def bill_calls_calc():
	bill_calls = bill_smses = 0
	for row in table:
		if row[1] == phone_number:
			if float(row[3]) > 20: 
				bill_calls += ( float(row[3]) - call_out_free_each ) * call_out_rate
			bill_smses += float(row[4])  * sms_out_rate
	return bill_calls, bill_smses

table = []
call_in_rate = 0
call_out_rate = 2
call_out_free_each = 20
sms_out_rate = 2
phone_number = '933156729'

# Генератор двумерного списка (таблицы) из файла csv
file_in = open('data.csv', 'r')
[table.append(string.rstrip().split(',')) for string in file_in]
file_in.close()

bill_calls, bill_smses = bill_calls_calc()

print('Затраты абонента с номером', phone_number, 'составляют:', bill_calls + bill_smses, 'рублей')
# os.system("pause")

a = input()
print(a)
exit(0)