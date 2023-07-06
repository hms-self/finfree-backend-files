import csv

with open('98)ihracat_orani.csv', 'r') as p_file:
    with open('29)ozsermaye_karllilik_orani.csv', 'r') as p_file1:
        with open('30)yatirim_sermayesi_getirisi_ROIC.csv', 'r') as p_file2:
            reader2=csv.reader(p_file2, delimiter=';' )
            reader1=csv.reader(p_file1, delimiter=';' )
            reader=csv.reader(p_file, delimiter=';')
            lists=list(reader)
            lists1=list(reader1)
            lists2=list(reader2)


            def check(list1, val):
                return (all(x > val for x in list1))

            for i in range(1,350):
                a=[] #son 5 yıl çeyreklik bazda ihracat oranları
                for j in range(len(lists[i][-18:])):
                    a.extend([float(lists[i][-18:][j].replace('%',''))])

                toplam=0
                for k in a:
                    toplam+=k
                ortalama_ihracat=toplam/18

                b=[] #son 5 yıl çeyreklik bazda ROE
                for j in range(len(lists1[i][-19:-1])):
                    b.extend([float(lists1[i][-19:-1][j].replace('%', ''))])
                toplamm = 0
                for k in b:
                    toplamm+=k
                ortalama_roe=toplamm/18

                c=[] #son 5 yıl çeyreklik bazda ROIC
                for j in range(len(lists2[i][-19:-1])):
                    c.extend([float(lists2[i][-19:-1][j].replace('%', ''))])
                toplammm = 0
                for k in c:
                    toplammm+=k
                ortalama_roic=toplammm/18


                if ortalama_ihracat>10:
                    if ortalama_roe>10:
                        if ortalama_roic>10:
                            print(lists[i][0])


