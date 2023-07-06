import csv
with open('76)firma_degeri_yeni.csv', 'r') as reader_file1:
    with open('1)hasılat_.csv', 'r') as reader_file2:
        with open('sanaiyes.csv', 'r') as p_file:
            with open('fd_satislar.csv', 'w') as n_file:
                writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
                reader = csv.reader(p_file, delimiter=';')
                reader1= csv.reader(reader_file1, delimiter=';' )
                reader2=csv.reader(reader_file2, delimiter=';')
                lists=list(reader)
                lists1=list(reader1)
                lists2=list(reader2)

                for i in range(1,46):

                    lists[0].extend([lists1[0][i]]) #tarihler

                for m in range(1, 351):
                    for l in range(1,46):
                        try:
                            fd_favok = round(((float(lists1[m][l].replace(',','.')) / (
                                float(lists2[m][l].replace('.','').replace(',','.'))))), 2)

                        except ZeroDivisionError:
                            fd_favok = 0


                        lists[m].extend([str(fd_favok)])

                writer.writerows(lists)

