import csv
import os

with open('2020 sanai 6.csv', 'r',
          encoding='utf-8-sig') as reader_file1:
    with open('faaliyet_kar_marji2.csv',
              'r') as p_file:  # bir öncekini oku
        with open('faaliyet_kar_marji3.csv',
                  'w') as n_file:  # üstüne yeni columnlar ekle

            writer = csv.writer(n_file,
                                delimiter=';',
                                lineterminator='\n')
            reader = csv.reader(p_file,
                                delimiter=';')
            reader1 = csv.reader(reader_file1,
                                 delimiter=';')

            lists = list(reader)
            lists1 = list(reader1)

            all = []
            all.extend([lists1])
            for m in range(1):
                lists[0].extend([all[m][0][1]])

            for k in range(1):
                for j in range(1,351):
                    try:
                        faaliyet_kar_marji=round(((float(all[k][350][j].replace('.','').replace(',','.')[:-3])/(float(all[k][315][j].replace('.','').replace(',','.')[:-3]))))*100,2)

                    except ZeroDivisionError:
                        faaliyet_kar_marji=0
                lists[j].extend(['%'+str(faaliyet_kar_marji)])


            writer.writerows(lists)

