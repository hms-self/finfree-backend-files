import csv

with open('büyüme yıllık.csv', 'r') as reader_file:
    with open('sanaiyes.csv', 'r') as p_file:
        with open('favok_ebitda_büyüme.csv', 'w') as n_file:
            writer = csv.writer(n_file, delimiter=';', lineterminator='\n')
            reader = csv.reader(p_file, delimiter=';')
            reader1= csv.reader(reader_file, delimiter=';' )
            lists=list(reader)
            lists1=list(reader1)

            for i in range(-46,-56,-1):

                lists[0].extend([lists1[2][i]]) #tarihler

            for k in range(1, 351):
                l=k+2
                for j in range(-46,-56,-1):
                    lists[k].extend([lists1[l][j]])

            writer.writerows(lists)

