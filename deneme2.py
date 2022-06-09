import csv
with open ('2012 sanai 12.csv' ,'r', encoding='utf-8-sig') as reader_file1:
    with open('2013 sanai 3.csv', 'r', encoding='utf-8-sig') as reader_file2:
        with open('2013 sanai 6.csv', 'r', encoding='utf-8-sig') as reader_file3:
            with open('2013 sanai 9.csv', 'r', encoding='utf-8-sig') as reader_file4:
                with open('2013 sanai 12.csv', 'r', encoding='utf-8-sig') as reader_file5:
                    with open('2014 sanai 3.csv', 'r', encoding='utf-8-sig') as reader_file6:
                        with open('2014 sanai 6.csv', 'r', encoding='utf-8-sig') as reader_file7:
                            with open('2014 sanai 9.csv', 'r', encoding='utf-8-sig') as reader_file8:
                                with open('2014 sanai 12.csv', 'r', encoding='utf-8-sig') as reader_file9:
                                    with open('2015 sanai 3.csv', 'r', encoding='utf-8-sig') as reader_file10:
                                        with open('2015 sanai 6.csv', 'r', encoding='utf-8-sig') as reader_file11:
                                            with open('2015 sanai 9.csv', 'r', encoding='utf-8-sig') as reader_file12:
                                                with open('2015 sanai 12.csv', 'r',
                                                          encoding='utf-8-sig') as reader_file13:
                                                    with open('2016 sanai 3.csv', 'r',
                                                              encoding='utf-8-sig') as reader_file14:
                                                        with open('2016 sanai 6.csv', 'r',
                                                                  encoding='utf-8-sig') as reader_file15:


                                                                with open('hasılat.csv', 'r') as p_file: #bir öncekini oku
                                                                    with open('hasılat2.csv', 'w') as n_file: #üstüne yeni columnlar ekle
-----------------------------------------------------------------------------------------------
import csv
import os

with open('2020 sanai 6.csv', 'r',
          encoding='utf-8-sig') as reader_file1:
    with open('faaliyet_kari2.csv',
              'r') as p_file:  # bir öncekini oku
        with open('faaliyet_kari3.csv',
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