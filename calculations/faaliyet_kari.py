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


                                                                with open('sanaiyes.csv', 'r') as p_file: #bir öncekini oku
                                                                    with open('faaliyet_kari1.csv', 'w') as n_file: #üstüne yeni columnlar ekle

                                                                        writer = csv.writer(n_file, delimiter=';',lineterminator='\n')
                                                                        reader=csv.reader(p_file, delimiter=';')
                                                                        reader1 = csv.reader(reader_file1, delimiter=';')
                                                                        reader2 = csv.reader(reader_file2, delimiter=';')
                                                                        reader3 = csv.reader(reader_file3, delimiter=';')
                                                                        reader4 = csv.reader(reader_file4, delimiter=';')
                                                                        reader5 = csv.reader(reader_file5, delimiter=';')
                                                                        reader6 = csv.reader(reader_file6, delimiter=';')
                                                                        reader7 = csv.reader(reader_file7, delimiter=';')
                                                                        reader8 = csv.reader(reader_file8, delimiter=';')
                                                                        reader9 = csv.reader(reader_file9, delimiter=';')
                                                                        reader10 = csv.reader(reader_file10, delimiter=';')
                                                                        reader11 = csv.reader(reader_file11, delimiter=';')
                                                                        reader12 = csv.reader(reader_file12, delimiter=';')
                                                                        reader13 = csv.reader(reader_file13, delimiter=';')
                                                                        reader14 = csv.reader(reader_file14, delimiter=';')
                                                                        reader15 = csv.reader(reader_file15, delimiter=';')

                                                                        lists = list(reader)
                                                                        lists1 = list(reader1)
                                                                        lists2 = list(reader2)
                                                                        lists3 = list(reader3)
                                                                        lists4 = list(reader4)
                                                                        lists5 = list(reader5)
                                                                        lists6 = list(reader6)
                                                                        lists7 = list(reader7)
                                                                        lists8 = list(reader8)
                                                                        lists9 = list(reader9)
                                                                        lists10 = list(reader10)
                                                                        lists11 = list(reader11)
                                                                        lists12 = list(reader12)
                                                                        lists13 = list(reader13)
                                                                        lists14 = list(reader14)
                                                                        lists15 = list(reader15)

                                                                        all=[]
                                                                        all.extend([lists1,lists2,lists3,lists4,lists5,lists6,lists7,lists8,lists9,lists10,lists11,lists12,lists13,lists14,lists15])

                                                                        for m in range(15):
                                                                            lists[0].extend([all[m][0][1]])

                                                                        for k in range(15):
                                                                            for i in range(1, 351):
                                                                                lists[i].extend([all[k][350][i]])


                                                                        writer.writerows(lists)

