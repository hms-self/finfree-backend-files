import csv
with open('9)hisse_sayisi.csv', 'r') as reader_file:
    with open('13)serbest_nakit_akisi.csv', 'r') as reader_file1:
        with open('sanaiyes.csv', 'r') as p_file:
            with open('hisse_basi_serbest_nakit_akisi.csv', 'w') as n_file:
                writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
                reader = csv.reader(p_file, delimiter=';')
                reader1= csv.reader(reader_file, delimiter=';' )
                reader2=csv.reader(reader_file1, delimiter=';')
                lists=list(reader)
                lists1=list(reader1)
                lists2=list(reader2)

                for i in range(1,45):

                    lists[0].extend([lists1[0][i]]) #tarihler

                for m in range(1, 351):
                    for l in range(1,46):
                        try:
                            hisse_basi_serbest_nakit_akis = round(((float(lists2[m][l].replace('.', '').replace(',', '.')[:-3]) / (
                                float(lists1[m][l].replace('.', '').replace(',', '.')[:-3])))), 2)

                        except ZeroDivisionError:
                            hisse_basi_serbest_nakit_akis = 0
                        except ValueError:
                            hisse_basi_serbest_nakit_akis = 0

                        lists[m].extend([str(hisse_basi_serbest_nakit_akis).replace('.', ',')])

                writer.writerows(lists)

