import pandas as pd
import csv
import plistlib
import xml.etree.ElementTree as et

# conversion xlsx in to csv
# read_file = pd.read_excel('DominiGames Test  Sheet.xlsx')
# read_file.to_csv('conv_from_xsls.csv', index=False, header=True)

# чтение файла.cvs
list_Fl_xlsx_to_csv = []  # list заголовков файла csv (конверт из xlsx)
with open('conv_from_xsls.csv') as f:
    f_read = csv.reader(f)
    for row in f_read:
        list_Fl_xlsx_to_csv = row  # запись заголовка в словарь list_Fl_xlsx_to_csv
        break  # вывод только заголовка
print('list_Fl_xlsx_to_csv - ', list_Fl_xlsx_to_csv)

# чтение файла.plist (MacOC)
list_Fl_plist = []  # list ключей файла plist
with open('/home/dikson/PycharmProjects/Test_Project/Tests_DominiGames/valid_tables/Info.plist', 'rb') as fp:
    pl = plistlib.load(fp)
    list_Fl_plist = list(pl.keys())
print('list_Fl_plist - ', list_Fl_plist)

# чтение файла xml
list_Fl_xml = []  # list ключей файла xml
tree = et.parse('DominiIAP.xml')
data = tree.getroot()
for item in data:
    if item.tag == "shop_items":
        for item_child in item:
            if item_child.tag == 'item':
                for i in item_child:
                    list_Fl_xml.append(i.tag)
                break
print('list_Fl_xml - ', list_Fl_xml)

print(f'Проверка на валидность таблиц CSV и XML')
for i in range(len(list_Fl_xlsx_to_csv)):
    if list_Fl_xlsx_to_csv[i] != list_Fl_xml[i]:
        print('Поля не совпадают, в исходной таблице ключ - ', list_Fl_xlsx_to_csv[i], ', в проверяемой - ',
              list_Fl_xml[i])
if len(list_Fl_xlsx_to_csv) != len(list_Fl_xml):
    print('Количество полей с ключами в таблицах не совпадает')

print(f'Проверка на валидность таблиц CSV и PLIST')
for i in range(len(list_Fl_xlsx_to_csv)):
    if list_Fl_xlsx_to_csv[i] != list_Fl_plist[i]:
        print('Поля не совпадают, в исходной таблице ключ - ', list_Fl_xlsx_to_csv[i], ', в проверяемой - ',
              list_Fl_plist[i])
if len(list_Fl_xlsx_to_csv) != len(list_Fl_plist):
    print('Количество полей с ключами в таблицах не совпадает')
