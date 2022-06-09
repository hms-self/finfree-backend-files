import csv

with open('99)favok_ebitda_büyüme.csv', 'r') as p_file:
    with open('100)satislar_büyüme.csv', 'r') as p_file2:
        with open('net_kar_büyüme.csv', 'r') as p_file3:
            with open('sanaiyes.csv', 'r') as p_file1:
                with open('büyüme_ort.csv', 'w') as n_file:
                    writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
                    reader3=csv.reader(p_file3, delimiter=';')
                    reader2=csv.reader(p_file2, delimiter=';')
                    reader1= csv.reader(p_file1, delimiter=';')
                    reader = csv.reader(p_file, delimiter=';')
                    lists=list(reader)
                    lists2=list(reader2)
                    lists3=list(reader3)


                    lists1=list(reader1)


                    for i in range(1,351):
                        a=[]
                        for j in range(1,11):
                            try:
                                a.extend([float(lists[i][:][j].replace('%','').replace(',','.'))])

                            except ValueError:
                                break
                        toplam=0
                        for k in a:
                            toplam+=k
                        ort_favok_buyume=round(float(toplam/10),2)
                        b=[]
                        for j in range(1,11):
                            try:
                                b.extend([float(lists2[i][:][j].replace('%','').replace(',','.'))])
                            except ValueError:
                                break
                        toplamm=0
                        for k in a:
                            toplamm+=k
                        ort_satislar_buyume=round(float(toplamm/10),2)
                        c=[]
                        for j in range(1,11):
                            try:
                                c.extend([float(lists3[i][:][j].replace('%','').replace(',','.'))])
                            except ValueError:
                                break
                        toplammm=0
                        for k in a:
                            toplammm+=k
                        ort_net_kar_buyume=round(float(toplammm/10),2)

                        lists1[i].extend([(ort_favok_buyume+ort_net_kar_buyume+ort_satislar_buyume)/3])




                    writer.writerows(lists1)


