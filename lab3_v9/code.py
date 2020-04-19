import lab1
import lab2
from number_to_text import decimal2text
import decimal
from fpdf import FPDF
import datetime
import sys

phone_number, call_in_total, call_out_total, sms_total, call_in_rate, call_out_rate, sms_rate = lab1.lab1_main()
ip_client, mbit_total, mbit_rate = lab2.lab2_main()
int_units = ((u'рубль', u'рубля', u'рублей'), 'm')
exp_units = ((u'копейка', u'копейки', u'копеек'), 'f')

date = datetime.date.today()

pdf = FPDF()
pdf.set_margins(13, 13)
pdf.add_page()

pdf.add_font('Arial', '', 'C:\\Windows\\Fonts\\arial.ttf', True)
pdf.add_font('Arial Bold', '', 'C:\\Windows\\Fonts\\arialbd.ttf', True)
pdf.set_font('Arial', '', 8)

# Банк, БИК, Пусто
pdf.cell(95, 15, '', 1, 0)
pdf.cell(15, 5, 'БИК', 1, 0)
pdf.cell(60, 15, '', 1, 0)
pdf.cell(0, 0, '', 0, 1)
pdf.cell(95, 5, 'Сбербанк России ОАО г. Санкт-Петербург', 0, 0)
pdf.cell(15, 5, '', 0, 0)
pdf.cell(60, 5, '044525225', 0, 1)
pdf.cell(95, 5, '', 0, 0)
pdf.cell(15, 5, 'Сч. №', 0, 0)
pdf.cell(60, 5, '30101810400000000225', 0, 1)
pdf.cell(95, 5, 'Банк получателя', 0, 1)
pdf.cell(0, -10, '', 0, 1)
# Сч.
pdf.cell(95, 15, '', 0, 0)
pdf.cell(15, 10, '', 1, 1)

# ИНН, КПП, Сч, Пусто
pdf.cell(55, 5, 'ИНН    '+'502204278650', 1, 0)
pdf.cell(40, 5, 'КПП    '+'10', 1, 0)
pdf.cell(15, 20, '', 1, 0)
pdf.cell(60, 20, '', 1, 0)
pdf.cell(0, 0, '', 0, 1)
pdf.cell(95, 5, '', 0, 0)
pdf.cell(15, 5, 'Сч. №', 0, 0)
pdf.cell(60, 5, '40802810740200101005', 0, 1)
pdf.cell(95, 5, '"ИП Яресько Степан Антонович"', 0, 1)
pdf.cell(95, 5, '', 0, 1)
pdf.cell(95, 5, 'Получатель', 0, 0)
pdf.cell(0, -10, '', 0, 1)
# Получатель
pdf.cell(95, 15, '', 1, 1)

# Счет на оплату
pdf.set_font('Arial Bold', '', 14)
pdf.cell(170, 16, 'Счет на оплату № '+'777'+' от '+str(date.day)+'.'+str(date.month)+'.'+str(date.year)+' г.', 0, 1)

# Линия
pdf.cell(170, 0, '', 1, 1)

# Поставщик
pdf.set_font("Arial", '', 9)
pdf.cell(170, 5, '', 0, 1)
pdf.cell(30, 5, 'Поставщик', 0, 0)
pdf.cell(140, 10, 'ИНН 5022017021 КПП 502 "Фонд Инновационных Открытий", г. Москва', 0, 0)
pdf.cell(0, 5, '', 0, 1)
# Исполнитель
pdf.cell(30, 5, '(Исполнитель):', 0, 1)

# Покупатель
pdf.cell(170, 5, '', 0, 1)
pdf.cell(30, 5, 'Покупатель', 0, 0)
pdf.cell(140, 10, 'ИНН 502204278650 КПП 10 "ИП Яресько Степан Антонович", г. Санкт-Петербург', 0, 0)
pdf.cell(0, 5, '', 0, 1)
# Заказчик
pdf.cell(30, 5, '(Заказчик):', 0, 1)

# Основание
pdf.cell(170, 5, '', 0, 1)
pdf.cell(30, 5, 'Основание:', 0, 0)
pdf.cell(140, 5, 'Договор №007', 0, 1)
pdf.cell(170, 5, '', 0, 1)

# Таблица услуг заголовок
pdf.set_font('Arial Bold', '', 9)
pdf.cell(10, 5, '№', 1, 0, 'C')
pdf.cell(80, 5, 'Товары (работы, услуги)', 1, 0, 'C')
pdf.cell(20, 5, 'Кол-во', 1, 0, 'C')
pdf.cell(10, 5, 'Ед.', 1, 0, 'C')
pdf.cell(25, 5, 'Цена', 1, 0, 'C')
pdf.cell(25, 5, 'Сумма', 1, 1, 'C')

# Таблица услуг Входящие
pdf.set_font('Arial', '', 9)
pdf.cell(10, 10, '1', 1, 0, 'C')
pdf.cell(80, 10, 'Входящие звонки на номер '+str(phone_number), 1, 0)
pdf.cell(20, 10, str(call_in_total), 1, 0, 'R')
pdf.cell(10, 10, 'мин.', 1, 0, 'R')
pdf.cell(25, 10, str(float(call_in_rate)), 1, 0, 'R')
pdf.cell(25, 10, str(float(call_in_total*call_in_rate)), 1, 1, 'R')

# Таблица услуг Исходящие
pdf.cell(10, 10, '2', 1, 0, 'C')
pdf.cell(80, 10, 'Исходящие звонки с номера '+str(phone_number), 1, 0)
pdf.cell(20, 10, str(call_out_total), 1, 0, 'R')
pdf.cell(10, 10, 'мин.', 1, 0, 'R')
pdf.cell(25, 10, str(float(call_out_rate)), 1, 0, 'R')
pdf.cell(25, 10, str(float(call_out_total*call_out_rate)), 1, 1, 'R')

# Таблица услуг СМС
pdf.cell(10, 10, '3', 1, 0, 'C')
pdf.cell(80, 10, 'Исходящие СМС с номера '+str(phone_number), 1, 0)
pdf.cell(20, 10, str(int(sms_total)), 1, 0, 'R')
pdf.cell(10, 10, 'шт.', 1, 0, 'R')
pdf.cell(25, 10, str(float(sms_rate)), 1, 0, 'R')
pdf.cell(25, 10, str(float(sms_total*sms_rate)), 1, 1, 'R')

# Таблица услуг Трафик
pdf.cell(10, 10, '4', 1, 0, 'C')
pdf.cell(80, 10, 'Исходящие интернет трафик с IP '+str(ip_client), 1, 0)
pdf.cell(20, 10, str(mbit_total), 1, 0, 'R')
pdf.cell(10, 10, 'Мб.', 1, 0, 'R')
pdf.cell(25, 10, str(float(mbit_rate)), 1, 0, 'R')
pdf.cell(25, 10, str(float(mbit_total*mbit_rate)), 1, 1, 'R')

# Итого
total = call_in_total*call_in_rate+call_out_total*call_out_rate+sms_total*sms_rate+mbit_total*mbit_rate
pdf.cell(110, 5, '', 0, 1)
pdf.set_font('Arial Bold', '', 9)
pdf.cell(110, 5, '', 0, 0)
pdf.cell(35, 5, 'Итого: ', 0, 0, 'R')
pdf.cell(25, 5, str(total), 0, 1, 'R')

# Итого
pdf.cell(110, 5, '', 0, 0)
pdf.cell(35, 5, 'В том числе НДС: ', 0, 0, 'R')
pdf.cell(25, 5, str(0.2*(total)), 0, 1, 'R')

# Итого
pdf.cell(110, 5, '', 0, 0)
pdf.cell(35, 5, 'Всего к оплате: ', 0, 0, 'R')
pdf.cell(25, 5, str(total), 0, 1, 'R')

# Всего наименований
pdf.set_font('Arial', '', 9)
pdf.cell(170, 5, '', 0, 1)
pdf.cell(170, 5, 'Всего наименований '+'4'+' на сумму '+str(total)+' руб.', 0, 1)

#Сумма прописью
pdf.set_font('Arial Bold', '', 9)
pdf.cell(170, 5, 'Сумма прописью: '+ decimal2text(decimal.Decimal(str(total)), int_units=int_units, exp_units=exp_units), 0, 1)

# Внимание
pdf.set_font('Arial', '', 9)
pdf.cell(170, 5, '', 0, 1)
pdf.cell(170, 5, 'Внимание!', 0, 1)
pdf.cell(170, 5, 'Оплата данного счета означает согласие с условиями поставки товара.', 0, 1)
pdf.cell(170, 5, 'Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.', 0, 1)
pdf.cell(170, 5, 'Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии доверенности и', 0, 1)
pdf.cell(170, 5, 'паспорта.', 0, 1)
pdf.cell(170, 5, '', 0, 1)
# Линия
pdf.cell(170, 0, '', 1, 1)

#Руководитель бухгалтер
pdf.cell(170, 5, '', 0, 1)
pdf.set_font('Arial Bold', '', 9)
pdf.cell(170, 5, 'Руководитель      ______________________________________         Бухгалтер      _________________________', 0, 1)

pdf.output('client_bill.pdf')

sys.exit(0)