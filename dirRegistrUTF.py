import os

import chardet

path = '//home/dikson/test_dir'  # переменная с рабочей директорией


def register_chang(path):
    for i in os.listdir(path):
        file_search(path + '/' + i)
        if os.path.isdir(path + '/' + i):
            register_chang(path + '/' + i)

        os.chdir(path)  # переход в рабочую директорию
        os.rename(i, i.upper())  # изменение регистра файла


def file_search(t):
    if os.path.isfile(t):
        encod_utf(t)


def encod_utf(file):
    with open(file, 'rb') as f:
        data = f.read()
        data_char = chardet.detect(data).get('encoding')

        if data_char != None:
            data_dec = data.decode(data_char)
            data_enc = data_dec.encode('utf-8')
            with open(data, 'wb') as fw:
                fw.write(data_enc)
            print('файл сконвертирован, перезаписан - ', fw)

        else:
            print('Файл не конвертируемый', f)


register_chang(path)

# if __name__ == '__main__':
# path = input('ВВЕДИТЕ ПУТЬ ДО КАТАЛОГА СОРТИРОВКИ -')
# register_chang(path)
