import csv
import os

with open('2020 sanai 6.csv', 'r',
          encoding='utf-8-sig') as reader_file1:
    with open('net_kar2.csv',
              'r') as p_file:  # bir öncekini oku
        with open('net_kar3.csv',
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
                for i in range(1, 351):
                    lists[i].extend([str(all[k][345][i])])



            writer.writerows(lists)