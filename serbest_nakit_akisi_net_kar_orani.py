import csv
with open('13)serbest_nakit_akisi.csv', 'r') as reader_file1:
    with open('5)net_kar.csv', 'r') as reader_file2:
        with open('sanaiyes.csv', 'r') as p_file:
            with open('serbest_nakit_akisi_net_kar_oranı.csv', 'w') as n_file:
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
                            fcf_net_kar = round(((float(lists1[m][l].replace('.', '').replace(',', '.')[:-3]) / (
                                float(lists2[m][l].replace('.', '').replace(',', '.')[:-3])))), 2)

                        except ZeroDivisionError:
                            fcf_net_kar = 0
                        except ValueError:
                            fcf_net_kar = 0

                        lists[m].extend([str(fcf_net_kar).replace('.', ',')])

                writer.writerows(lists)

