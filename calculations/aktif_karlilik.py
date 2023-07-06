import csv
with open('25)net_kar_marji.csv', 'r') as reader_file1:
    with open('26)ort_varlik_devir_hizi_yeni1.csv', 'r') as reader_file2:
        with open('sanaiyes.csv', 'r') as p_file:
            with open('aktif_karlilik_yeni.csv', 'w') as n_file:
                writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
                reader = csv.reader(p_file, delimiter=';')
                reader1= csv.reader(reader_file1, delimiter=';' )
                reader2=csv.reader(reader_file2, delimiter=';')
                lists=list(reader)
                lists1=list(reader1)
                lists2=list(reader2)

                for i in range(1,42):

                    lists[0].extend([lists2[0][i]]) #tarihler

                for m in range(1, 351):
                    for l in range(1,42):
                        try:
                            aktif_karlilik = round(((float(lists1[m][l+4][1:]) * (
                                float(lists2[m][l].replace(',', '.'))))), 2)

                        except ZeroDivisionError:
                            aktif_karlilik = 0
                        except ValueError:
                            aktif_karlilik = 0

                        lists[m].extend([str(aktif_karlilik)])

                writer.writerows(lists)

