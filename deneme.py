import csv
with open ('2009 Banka 3.csv' ,'r', encoding='utf-8-sig') as reader_file1:
    with open('2009 Banka 6.csv', 'r', encoding='utf-8-sig') as reader_file2:
        with open('2009 Banka 9.csv', 'r', encoding='utf-8-sig') as reader_file3:
            with open('2009 Banka 12.csv', 'r', encoding='utf-8-sig') as reader_file4:
                with open('2010 Banka 03.csv', 'r', encoding='utf-8-sig') as reader_file5:
                    with open('2010 Banka 06.csv', 'r', encoding='utf-8-sig') as reader_file6:
                        with open('2010 Banka 09.csv', 'r', encoding='utf-8-sig') as reader_file7:
                            with open('2010 Banka 12.csv', 'r', encoding='utf-8-sig') as reader_file8:
                                with open('2011 Banka 03.csv', 'r', encoding='utf-8-sig') as reader_file9:
                                    with open('2011 Banka 06.csv', 'r', encoding='utf-8-sig') as reader_file10:
                                        with open('2011 Banka 09.csv', 'r', encoding='utf-8-sig') as reader_file11:
                                            with open('2011 Banka 12.csv', 'r', encoding='utf-8-sig') as reader_file12:
                                                with open('2012 Banka 03.csv', 'r',
                                                          encoding='utf-8-sig') as reader_file13:
                                                    with open('2012 Banka 06.csv', 'r',
                                                              encoding='utf-8-sig') as reader_file14:
                                                        with open('2012 Banka 09.csv', 'r',
                                                                  encoding='utf-8-sig') as reader_file15:
                                                            with open('2012 Banka 12.csv', 'r',
                                                                      encoding='utf-8-sig') as reader_file16:

                                                                with open('new_yes.csv', 'r') as p_file: #bir öncekini oku
                                                                    with open('new_yes1.csv', 'w') as n_file: #üstüne yeni columnlar ekle

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
                                                                        reader16 = csv.reader(reader_file16, delimiter=';')

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
                                                                        lists16 = list(reader16)


                                                                        lists=list(reader)

                                                                        lists[0].extend([lists1[0][1],lists2[0][1],lists3[0][1],lists4[0][1],lists5[0][1],lists6[0][1],lists7[0][1],lists8[0][1],lists9[0][1],lists10[0][1],lists11[0][1],lists12[0][1],lists13[0][1],lists14[0][1],lists15[0][1],lists16[0][1]]) #adding a new date in header (güncelle 'lists1')

                                                                        for i in range(1,15):
                                                                            lists[i].extend([lists1[6][i],lists2[6][i],lists3[6][i],lists4[6][i],lists5[6][i],lists6[6][i],lists7[6][i],lists8[6][i],lists9[6][i],lists10[6][i],lists11[6][i],lists12[6][i],lists13[6][i],lists14[6][i],lists15[6][i],lists16[6][i]]) #appendin içindeki istediğim value lar...

                                                                        print(lists1)
