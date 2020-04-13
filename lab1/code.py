import os
import math

#============================================================================================
# Функция поиска записей о действиях абонента и подсчета стоимости услуг вх/исх звонков и смс
def bills_calc():

	bill_call_in_total = bill_call_out_total = bill_sms_total = 0
	call_in_total = call_out_total = sms_total = 0

	# Подсчет всего вх/исх звонков и смс с вычетом бесплатных на каждой операции
	for row in table:
		if row[1] == phone_number:
			if float(row[3]) > call_out_free_each: 
				call_out_total += math.ceil( float(row[3]) - call_out_free_each )
			if float(row[4]) > sms_free_each:
				sms_total += float(row[4]) - sms_free_each
		if row[2] == phone_number:
			if float(row[3]) > call_in_free_each: 
				call_in_total += math.ceil( float(row[3]) - call_in_free_each )

	# Подсчет всего вх/исх звонков и смс с вычетом бесплатных за весь период
	if call_out_total > call_out_free_total:
		call_out_total = call_out_total - call_out_free_total
	else: call_out_total = 0
	if call_in_total > call_in_free_total:
		call_in_total = call_in_total - call_in_free_total
	else: call_in_total = 0
	if sms_total > sms_free_total:
		sms_total = sms_total - sms_free_total
	else: sms_total = 0

	# Подсчет стоимости вх/исх звонков и смс
	bill_call_in_total = call_in_total * call_in_rate
	bill_call_out_total = call_out_total * call_out_rate
	bill_sms_total = sms_total * sms_rate

	return bill_call_in_total, bill_call_out_total, bill_sms_total
#============================================================================================


#=================================
# Переменные
table = []
call_in_rate = 0
call_in_free_each = 0
call_in_free_total = 0
call_out_rate = 2
call_out_free_each = 0
call_out_free_total = 20
sms_rate = 2
sms_free_each = 0
sms_free_total = 0
phone_number_default = '933156729'
#=================================


#=====================================================================================
phone_number = input('Введите номер телефона (по умолчанию 933156729): ')
if phone_number == '': phone_number = phone_number_default
elif len(phone_number) < 9 or not phone_number.isdigit():
	print('Некорректно введен номер телефона:', phone_number)
	exit(-1)

# Генератор двумерного списка (таблицы) из файла csv
file_in = open('data.csv', 'r')
[table.append(string.rstrip().split(',')) for string in file_in]
file_in.close()

bill_call_in_total, bill_call_out_total, bill_sms_total = bills_calc()
bill_total = bill_call_in_total + bill_call_out_total + bill_sms_total

print('Затраты абонента с номером', phone_number, 'составляют:', bill_total, 'руб.')

os.system("pause")
#=====================================================================================