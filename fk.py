import csv

with open('oranlar 10 15.csv', 'r',encoding='utf-8-sig') as reader_file:
    with open('sanaiyes.csv', 'r', encoding='utf-8-sig') as p_file:
        with open('fk.csv', 'w') as n_file:
            with open('oranlar 15-20.csv', 'r', encoding='utf-8-sig') as reader_file2:
                writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
                reader = csv.reader(p_file, delimiter=';')
                reader1= csv.reader(reader_file, delimiter=';')
                reader2= csv.reader(reader_file2, delimiter=';')
                lists= list(reader)
                lists1= list(reader1)
                lists2\
                    = list(reader2)
                lists[0].extend(['2009/3','2009/6','2009/9'])


                for i in range(-106, -127, -1):
                    lists[0].extend([lists1[2][i]])  # tarihler

                for m in range(1, 351):
                    lists[m].extend(['0'] * 3)


                for k in range(1, 351):
                    l=k+2
                    for j in range(-85,-106,-1):
                        lists[k].extend([lists1[l][j]])

#ikinci dosya
                for i in range(-106, -127, -1):
                    lists[0].extend([lists2[3][i]])

                for k in range(1, 351):
                    l=k+3
                    for j in range(-85,-106,-1):
                        lists[k].extend([lists2[l][j]])

                writer.writerows(lists)





