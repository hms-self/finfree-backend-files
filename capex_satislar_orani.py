import csv
with open('12)capex.csv', 'r') as reader_file1:
    with open('1)hasılat_.csv', 'r') as reader_file2:
        with open('sanaiyes.csv', 'r') as p_file:
            with open('capex_satislar.csv', 'w') as n_file:
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
                            capex_satislar = round(((float(lists1[m][l].replace('.', '').replace(',', '.')[:-3]) / (
                                float(lists2[m][l].replace('.', '').replace(',', '.')[:-3])))), 2)

                        except ZeroDivisionError:
                            capex_satislar = 0
                        except ValueError:
                            capex_satislar = 0

                        lists[m].extend([str(capex_satislar).replace('.', ',')])

                writer.writerows(lists)

