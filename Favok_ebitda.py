import csv
with open('esas_faaliyet_kari.csv', 'r') as reader_file1:
    with open('amortisman_ve_itfa.csv', 'r') as reader_file2:
        with open('sanaiyes.csv', 'r') as p_file:
            with open('FAVOK_EBITDA_deneme.csv', 'w') as n_file:
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
                            FAVOK_EBITDA = ((float(lists1[m][l].replace('.', '').replace(',', '.')) + (
                                float(lists2[m][l].replace('.', '').replace(',', '.')))))

                        except ZeroDivisionError:
                            FAVOK_EBITDA = 0
                        except ValueError:
                            FAVOK_EBITDA = 0

                        lists[m].extend([str(FAVOK_EBITDA).replace(
                            ',','.'
                        )])

                writer.writerows(lists)

