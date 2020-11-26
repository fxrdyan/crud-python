import os,sys
P = print
Oc = os.system
while True:
    P("")
    P("")
    c = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if c.lower() == 'q':
        break
    elif c.lower() == 'l':
        i = open('database.txt','r').read().splitlines()
        P(" ╔══════════════════════════════════════════════════════════════════╗")
        P(" ╠═══════════════════════════   LIST BAHAN   ═══════════════════════╣")
        P(" ╠══════════════════╦══════════════════╦══════════╦═════════╦═══════╣")
        P(" ║      NAMA        ║    KODE BAHAN    ║  JUMLAH  ║  HARGA  ║ TOTAL ║")
        P(" ╠══════════════════╬══════════════════╬══════════╬═════════╬═══════╣")
        for l in i:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
                nama,kode,jumlah,harga,total = l1.strip().split('|')
                P((' ║ ')+(nama[:15]).ljust(17,'.')+('║ ')+(kode).ljust(17)+('║ ')+(jumlah)+(' Kg').ljust(6)+('║ ')+(harga).ljust(8)+('║ ')+(total).ljust(6)+('║ '))
        P(" ╚══════════════════╩══════════════════╩══════════╩═════════╩═══════╝")
    elif c.lower() == 'd':
        u = open('database.txt','r').read().splitlines()
        target = int(input(' Masukan Kode : '))
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
                nama,kode,jumlah,harga,total = l1.strip().split('|')
                if int(kode) == int(target):
                    P('BERHASIL MENGHAPUS Data %s'%(target))
                    pass
                else:      
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')        
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("'","").replace("\\n', '", "\n").replace("'","").replace("\\n",'')
            new2.write(i2)
        new2.close()
    elif c.lower() == 'e':
        u = open('database.txt','r').read().splitlines()
        target = input(' Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
                na,ni,tu,uts,uas,akhir = l1.strip().split('|')
                if na == target:
                    P(' Mengedit Data %s'%(target))
                    while (True):
                        nama = input(" Nama Bahan: ")
                        if nama == '':
                            P(' Masukan Nama Bahan')
                        else:
                            break
                    while (True):
                        try:
                            kode  = int(input(" Kode Bahan  : "))
                            if kode == '':
                                P(' Masukan Kode dengan Angka')
                        except ValueError:
                            P(' Masukan Kode dengan Angka')                
                        else:
                            break
                    while (True):
                        try:
                            jumlah  = int(input(" Jumlah (Kg): "))
                            if jumlah == '':
                                P(' Masukan Jumlah dengan Angka')
                        except ValueError:
                            P(' Masukan Jumlah dengan Angka')                
                        else:
                            break
                    while (True):
                        try:
                            harga  = int(input(" Harga per Kg: "))
                            if harga == '':
                                P(' Masukan Harga dengan Angka')
                        except ValueError:
                            P(' Masukan Harga dengan Angka')                
                        else:
                            break
                    total = jumlah * harga
                    edit  =('\nNama Bahan : '+nama+'|Kode : '+str(kode)+'|Jumlah : '+str(jumlah)+'|Harga : '+str(harga)+'|Total : '+str(total)+'\n')
                    nm.append(edit+'\n')
                else:      
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')        
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n","\n")
            new2.write(i2+'\n')
        new2.close()
    elif c.lower() == 'a':
        i = open('database.txt','a')
        P(" Tambah Data Bahan")
        while (True):
            nama = input(" Nama Bahan: ")
            if nama == '':
                P(' Masukan Nama Bahan')
            else:
                break
        while (True):
            try:
                kode  = int(input(" Kode Bahan  : "))
                if kode == '':
                    P(' Masukan Kode dengan Angka')
            except ValueError:
                P(' Masukan Kode dengan Angka')                
            else:
                break
        while (True):
            try:
                jumlah  = int(input(" Jumlah (Kg): "))
                if jumlah == '':
                    P(' Masukan Jumlah dengan Angka')
            except ValueError:
                P(' Masukan Jumlah dengan Angka')                
            else:
                break
        while (True):
            try:
                harga  = int(input(" Harga per Kg: "))
                if harga == '':
                    P(' Masukan Harga dengan Angka')
            except ValueError:
                P(' Masukan Harga dengan Angka')                
            else:
                break
        total = jumlah * harga
        i.write('\nNama Bahan : '+nama+'|Kode : '+str(kode)+'|Jumlah : '+str(jumlah)+'|Harga : '+str(harga)+'|Total : '+str(total)+'\n')
        i.close()
        Oc("clear")
    else:
        P("Pilih menu yang tersedia")
