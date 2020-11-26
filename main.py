# -- encoding: utf-8 --
while True:
    print("")
    print("")
    menu = int(input("[1]Tampil    [2]Tambah   [3]Ubah    [4]Hapus   [5]Keluar"))
    if menu == 5:
        break
    elif menu == 1:
        i = open('database.txt','r').read().splitlines()
        print(" ╔══════════════════════════════════════════════════════════════════════════╗")
        print(" ╠══════════════════════════════   LIST BAHAN   ════════════════════════════╣")
        print(" ╠══════════════════╦══════════════════╦════════════╦═══════════╦═══════════╣")
        print(" ║      NAMA        ║    KODE BAHAN    ║   JUMLAH   ║   HARGA   ║   TOTAL   ║")
        print(" ╠══════════════════╬══════════════════╬════════════╬═══════════╬═══════════╣")
        for l in i:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
                nama,kode,jumlah,harga,total = l1.strip().split('|')
                print((' ║ ')+(nama[:15]).ljust(17,'.')+('║ ')+(kode).ljust(17)+('║ ')+(jumlah).ljust(2)+(' Kg').ljust(9)+('║ ')+(harga).ljust(10)+('║ ')+(total).ljust(10)+('║ '))
        print(" ╚══════════════════╩══════════════════╩════════════╩═══════════╩═══════════╝")
    elif menu == 4:
        u = open('database.txt','r').read().splitlines()
        print("")
        target = int(input(' Masukan Kode : '))
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
                nama,kode,jumlah,harga,total = l1.strip().split('|')
                if int(kode) == int(target):
                    print("")
                    print('Berhasil Menghapus Data %s'%(target))
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
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n",'')
            new2.write(i2)
        new2.close()
    elif menu == 3:
        u = open('database.txt','r').read().splitlines()
        print("")
        target = int(input(' Masukan Kode : '))
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
                nama,kode,jumlah,harga,total = l1.strip().split('|')
                if int(kode) == int(target):
                    print("")
                    print(' Mengedit Data %s'%(target))
                    print("")
                    while (True):
                        nama = input(" Nama Bahan: ")
                        if nama == '':
                            print(' Masukan Nama Bahan')
                        else:
                            break
                    while (True):
                        try:
                            jumlah  = int(input(" Jumlah (Kg): "))
                            if jumlah == '':
                                print(' Masukan Jumlah dengan Angka')
                        except ValueError:
                            print(' Masukan Jumlah dengan Angka')                
                        else:
                            break
                    while (True):
                        try:
                            harga  = int(input(" Harga per Kg: "))
                            if harga == '':
                                print(' Masukan Harga dengan Angka')
                        except ValueError:
                            print(' Masukan Harga dengan Angka')                
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
    elif menu == 2:
        i = open('database.txt','a')
        print("")
        print(" Tambah Data Bahan")
        print("")
        while (True):
            nama = input(" Nama Bahan: ")
            if nama == '':
                print(' Masukan Nama Bahan')
            else:
                break
        while (True):
            try:
                kode  = int(input(" Kode Bahan  : "))
                if kode == '':
                    print(' Masukan Kode dengan Angka')
            except ValueError:
                print(' Masukan Kode dengan Angka')                
            else:
                break
        while (True):
            try:
                jumlah  = int(input(" Jumlah (Kg): "))
                if jumlah == '':
                    print(' Masukan Jumlah dengan Angka')
            except ValueError:
                print(' Masukan Jumlah dengan Angka')                
            else:
                break
        while (True):
            try:
                harga  = int(input(" Harga per Kg: "))
                if harga == '':
                    print(' Masukan Harga dengan Angka')
            except ValueError:
                print(' Masukan Harga dengan Angka')                
            else:
                break
        total = jumlah * harga
        i.write('\nNama Bahan : '+nama+'|Kode : '+str(kode)+'|Jumlah : '+str(jumlah)+'|Harga : '+str(harga)+'|Total : '+str(total)+'\n')
        i.close()
    else:
        print("Pilih menu yang tersedia")
