import csv

with open ('13)serbest_nakit_akisi.csv' ,'r', encoding='utf-8-sig') as reader_file:
    with open('serbest_nakit_akisi_buyumesi.csv', 'w') as n_file:
        with open('sanaiyes.csv', 'r') as p_file:
            writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
            reader = csv.reader(p_file , delimiter=';')
            reader1= csv.reader(reader_file , delimiter=';')
            lists=list(reader)
            lists1=list(reader1)

            for i in range(1,46):
                lists[0].extend([lists1[0][i]])
            for m in range(1, 351):
                lists[m].extend(['0'])

            for m in range(1, 351):

                for n in range(2,46):
                    try:
                        serbest_nakit_akis_buyume = round(((float(lists1[m][n].replace('.', '').replace(',', '.')[:-3])) - (float(
                            lists1[m][n-1].replace('.', '').replace(',', '.')[:-3]))) / abs(float(
                            lists1[m][n-1].replace('.', '').replace(',', '.')[:-3])) * 100, 2)

                    except ZeroDivisionError:
                        serbest_nakit_akis_buyume = 0
                    except ValueError:
                        serbest_nakit_akis_buyume = 0

                    lists[m].extend(['%' + str(serbest_nakit_akis_buyume)])
            writer.writerows(lists)
