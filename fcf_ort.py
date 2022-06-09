import csv

with open('serbest_nakit_akisi.csv', 'r') as p_file:
    with open('sanaiyes.csv', 'r') as p_file1:
        with open('FCF_10_YILLIK_ORT.csv', 'w') as n_file:
            writer = csv.writer(n_file, delimiter=';', lineterminator='\n')

            reader1= csv.reader(p_file1, delimiter=';')
            reader = csv.reader(p_file, delimiter=';')
            lists=list(reader)
            lists1=list(reader1)


            for i in range(1,351):
                a=[]
                for j in range(8,46,4):
                   a.extend([float(lists[i][:][j].replace('.','').replace(',','.'))])
                toplam=0
                for k in a:
                    toplam+=k
                ort=round(float(toplam/10),2)

                lists1[i].extend([str(round(int(ort)/1000000,2)).replace('.',',')])

            writer.writerows(lists1)


