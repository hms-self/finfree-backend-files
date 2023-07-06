import csv

with open('price_sales.csv', 'r') as reader_file:
    with open('sanaiyes.csv', 'r') as p_file:
        with open('temettu_verimi.csv', 'w') as n_file:
            writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
            reader = csv.reader(p_file, delimiter=';')
            reader1= csv.reader(reader_file, delimiter=';' )
            lists=list(reader)
            lists1=list(reader1)

            lists[0].extend(['2009/3', '2009/6', '2009/9'])

            for i in range(-1,-43,-1):

                lists[0].extend([lists1[2][i]]) #tarihler

            for m in range (1,351):

                lists[m].extend(['0']*3)

            for k in range(1, 351):
                l=k+2
                for j in range(-1,-43,-1):
                    lists[k].extend([str('%') + str(round(float(lists1[l][j].replace(',','.')),2))])

            writer.writerows(lists)

