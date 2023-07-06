import csv
import os

all=[]

with open('sanaiyes.csv', 'r') as p_file:
    with open('faaliyetlerden_gelen_nakit_akis_buyume.csv', 'w') as n_file:
        writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
        reader = csv.reader(p_file, delimiter=';')
        lists=list(reader)
        for j in range(2010,2021):
                if j==2020:
                    for b in range(2020, 2021):
                        for n in range(3,6,3):
                            with open(str(b-1) + ' sanai ' + str(n) + '.csv', 'r', encoding='utf-8-sig') as reader_file1:
                                with open(str(b) + ' sanai ' + str(n) + '.csv', 'r',encoding='utf-8-sig') as reader_file2:
                                    reader1 = csv.reader(reader_file1, delimiter=';')
                                    reader2 = csv.reader(reader_file2, delimiter=';')
                                    lists1 = list(reader1)
                                    lists2 = list(reader2)
                                    lists[0].extend([lists2[0][1]])
                                    for m in range(1, 351):
                                        try:
                                            faaliyetlerden_gelen_nakit_akis_buyume = round(((float(
                                                lists2[511][m].replace('.', '').replace(',', '.')[:-3])) - (float(
                                                lists1[511][m].replace('.', '').replace(',', '.')[:-3]))) / abs(float(
                                                lists1[511][m].replace('.', '').replace(',', '.')[:-3])) * 100, 2)

                                        except ZeroDivisionError:
                                            faaliyetlerden_gelen_nakit_akis_buyume = 0
                                        lists[m].extend(['%' + str(faaliyetlerden_gelen_nakit_akis_buyume)])


                else:
                    for k in range(3, 13, 3):
                        with open(str(j-1) + ' sanai ' + str(k) + '.csv', 'r', encoding='utf-8-sig') as reader_file1:
                            with open(str(j) + ' sanai ' + str(k) + '.csv', 'r', encoding='utf-8-sig') as reader_file2:
                                reader1 = csv.reader(reader_file1, delimiter=';')
                                reader2 = csv.reader(reader_file2, delimiter=';')
                                lists1 = list(reader1) #bir önceki sene
                                lists2 = list(reader2) # bir sonraki sene
                                lists[0].extend([lists2[0][1]])

                                for m in range(1, 351):
                                    try:
                                        faaliyetlerden_gelen_nakit_akis_buyume = round(((float(lists2[511][m].replace('.', '').replace(',', '.')[:-3]))-(float(lists1[511][m].replace('.', '').replace(',', '.')[:-3])))/abs(float(lists1[511][m].replace('.', '').replace(',', '.')[:-3]))*100 , 2)

                                    except ZeroDivisionError:
                                        faaliyetlerden_gelen_nakit_akis_buyume = 0

                                    lists[m].extend(['%'+str(faaliyetlerden_gelen_nakit_akis_buyume)])

        writer.writerows(lists)