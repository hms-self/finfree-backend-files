import csv

with open('74)pddd.csv', 'r') as reader_file1:
    with open('sanaiyes.csv', 'r') as p_file:
        with open('97)ozsermaye.csv', 'r') as reader_file2:
            with open('6)hisse_basi_kar_yeni.csv', 'r') as reader_file3:

                with open('firma_degeri.csv', 'w') as n_file:

                    writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
                    reader = csv.reader(p_file, delimiter=';')
                    reader1= csv.reader(reader_file1, delimiter=';' )
                    reader2= csv.reader(reader_file2, delimiter=';' )
                    reader3= csv.reader(reader_file3, delimiter=';' )



                    lists=list(reader)
                    lists1=list(reader1)
                    lists2=list(reader2)
                    lists3=list(reader3)


                    lists[0].extend(lists1[0][1:]) #tarihler


                    for m in range(1, 351):
                        for l in range(1, 46):

                            fd = round( float( float(lists1[m][l].replace(',','.')) * float(lists2[m][l].replace('.','').replace(',','.')) ) , 2 )



                            lists[m].extend([fd])

                    writer.writerows(lists)



