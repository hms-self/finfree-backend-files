import csv
import os

all=[]

with open('sanaiyes.csv', 'r') as p_file:
    with open('ortalama_tahsil_suresi.csv', 'w') as n_file:
        writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
        reader = csv.reader(p_file, delimiter=';')
        lists=list(reader)
        for j in range(2009,2021):
                if j==2020:
                    for b in range(2020, 2021):
                        for n in range(3,9,3):
                            with open(str(b) + ' sanai ' + str(n) + '.csv', 'r', encoding='utf-8-sig') as reader_file1:
                                reader1 = csv.reader(reader_file1, delimiter=';')
                                lists1 = list(reader1)
                                lists[0].extend([lists1[0][1]])
                                for m in range(1, 351):
                                    try:
                                        ortalama_tahsil_suresi = round(360 / (
                                                    (float(lists1[315][m].replace('.', '').replace(',', '.')[:-3])) / (
                                                float(lists1[23][m].replace('.', '').replace(',', '.')[:-3]))), 2)

                                    except ZeroDivisionError:
                                        ortalama_tahsil_suresi = 0
                                    lists[m].extend([str(ortalama_tahsil_suresi).replace('.', ',')])


                else:
                    for k in range(3, 13, 3):
                        with open(str(j)+' sanai '+str(k)+'.csv', 'r',encoding='utf-8-sig') as reader_file1:
                            reader1 = csv.reader(reader_file1,delimiter=';')
                            lists1 = list(reader1)
                            lists[0].extend([lists1[0][1]])
                            for m in range(1, 351):
                                try:
                                    ortalama_tahsil_suresi = round(360/ ((float(lists1[315][m].replace('.','').replace(',', '.')[:-3]))/(float(lists1[23][m].replace('.','').replace(',', '.')[:-3]))), 2)

                                except ZeroDivisionError:
                                    ortalama_tahsil_suresi = 0
                                lists[m].extend([str(ortalama_tahsil_suresi).replace('.',',')])



        writer.writerows(lists)