while True:
   print("")
   print("")
   menu = int(input("[1]Tampil    [2]Tambah   [3]Ubah    [4]Hapus   [5]Keluar "))

#-----Keluar Program-----#
   if menu == 5:
       break

#-----Tampil Data-----#
   elif menu == 1:

#Membuka file txt untuk mengecek data
       i = open('database.txt','r').read().splitlines()

#Membuat Table untuk menampilkan data
       print(" ╔══════════════════════════════════════════════════════════════════════════╗")
       print(" ╠══════════════════════════════   LIST BAHAN   ════════════════════════════╣")
       print(" ╠══════════════════╦══════════════════╦════════════╦═══════════╦═══════════╣")
       print(" ║      NAMA        ║    KODE BAHAN    ║   JUMLAH   ║   HARGA   ║   TOTAL   ║")
       print(" ╠══════════════════╬══════════════════╬════════════╬═══════════╬═══════════╣")

#Perulangan Menampilkan Data
       for l in i:
           if l == '':
               pass
           else:
               l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
               nama,kode,jumlah,harga,total = l1.strip().split('|')
               print((' ║ ')+(nama[:15]).ljust(17,'.')+('║ ')+(kode).ljust(17)+('║ ')+(jumlah).ljust(2)+(' Kg').ljust(9)+('║ ')+(harga).ljust(10)+('║ ')+(total).ljust(10)+('║ '))
       print(" ╚══════════════════╩══════════════════╩════════════╩═══════════╩═══════════╝")

#-----Hapus Data-----#
   elif menu == 4:

#Membuka file txt untuk mengecek data
       u = open('database.txt','r').read().splitlines()
       print("")

#Memasukan Kode Bahan yang akan dihapus
       target = int(input(' Masukan Kode : '))
       nm = []

#Perulangan untuk mengecek data yang akan dihapus 
       for l in u:
           if l == '':
               pass
           else:
               l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
               nama,kode,jumlah,harga,total = l1.strip().split('|')

#Pengecekan kode(target) yang dimasukan sama dengan kode bahan yang ada di database
               if int(kode) == int(target):
                   print("")
                   print('Berhasil Menghapus Data %s'%(target))
                   pass
               else:     
                   nm.append(str(l)+'\n')

#Membaca file database.txt dan hapus data yang dipilih
       new = open('database.txt','w')       
       new.write(str(nm))
       new.close()
       new = open('database.txt','r').read().splitlines()
       new1 = open('database.txt','w')
       new1.close()
       new2 = open('database.txt','a')

#Mengganti data yang dihapus dengan element kosong
       for i in new:
           i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n",'')
           new2.write(i2)
       new2.close()

#-----Ubah Data-----#
   elif menu == 3:

#Membuka file txt untuk mengecek data
       u = open('database.txt','r').read().splitlines()
       print("")

#Memasukan Kode Bahan yang akan diubah
       target = int(input(' Masukan Kode : '))
       nm = []

#Perulangan untuk mengecek data yang akan diubah 
       for l in u:
           if l == '':
               pass
           else:
               l1 = l.replace('Nama Bahan : ','').replace('Kode : ','').replace('Jumlah : ','').replace('Harga : ','').replace('Total : ','')
               nama,kode,jumlah,harga,total = l1.strip().split('|')

#Pengecekan kode(target) yang dimasukan sama dengan kode bahan yang ada di database
               if int(kode) == int(target):
                   print("")
                   print(' Mengedit Data %s'%(target))
                   print("")

#Perulangan data yang akan diubah
                   while (True):
                       nama = input(" Nama Bahan: ")

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
                       if nama == '':
                           print(' Masukan Nama Bahan')
                       else:
                           break
                   while (True):
                       try:
                           jumlah  = int(input(" Jumlah (Kg): "))

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
                           if jumlah == '':
                               print(' Masukan Jumlah dengan Angka')
                       except ValueError:
                           print(' Masukan Jumlah dengan Angka')               
                       else:
                           break
                   while (True):
                       try:
                           harga  = int(input(" Harga per Kg: "))

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
                           if harga == '':
                               print(' Masukan Harga dengan Angka')
                       except ValueError:
                           print(' Masukan Harga dengan Angka')               
                       else:
                           break

#Mengitung total harga bahan yang akan ditampilkan di tabel
                   total = jumlah * harga

#Perintah untuk mengisi detail baru untuk data bahan yang dipilih
                   edit  =('\nNama Bahan : '+nama+'|Kode : '+str(kode)+'|Jumlah : '+str(jumlah)+'|Harga : '+str(harga)+'|Total : '+str(total)+'\n')

#Kemudian detail baru tersebut akan disimpan di variable list kosong yang sudah disiapkan
                   nm.append(edit+'\n')
               else:     
                   nm.append(str(l)+'\n')

#Membaca file database.txt dan hapus data yang dipilih
       new = open('database.txt','w')       
       new.write(str(nm))
       new.close()
       new = open('database.txt','r').read().splitlines()
       new1 = open('database.txt','w')
       new1.close()
       new2 = open('database.txt','a')

#Kode bagian ini sama dengan bagian di atas
       for i in new:
           i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n","\n")
           new2.write(i2+'\n')
       new2.close()

#Tambah Data
   elif menu == 2:

#Membuka file txt untuk mengecek data
       i = open('database.txt','a')
       print("")
       print(" Tambah Data Bahan")
       print("")

       while (True):
           nama = input(" Nama Bahan: ")

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
           if nama == '':
               print(' Masukan Nama Bahan')
           else:
               break
       while (True):
           try:
               kode  = int(input(" Kode Bahan  : "))

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
               if kode == '':
                   print(' Masukan Kode dengan Angka')
           except ValueError:
               print(' Masukan Kode dengan Angka')               
           else:
               break
       while (True):
           try:
               jumlah  = int(input(" Jumlah (Kg): "))

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
               if jumlah == '':
                   print(' Masukan Jumlah dengan Angka')
           except ValueError:
               print(' Masukan Jumlah dengan Angka')               
           else:
               break
       while (True):
           try:
               harga  = int(input(" Harga per Kg: "))

#Validasi inputan, jika data kosong program tidak akan dilanjutkan sampai data yang dimasukan benar
               if harga == '':
                   print(' Masukan Harga dengan Angka')
           except ValueError:
               print(' Masukan Harga dengan Angka')               
           else:
               break

#Mengitung total harga bahan yang akan ditampilkan di tabel
       total = jumlah * harga
       i.write('\nNama Bahan : '+nama+'|Kode : '+str(kode)+'|Jumlah : '+str(jumlah)+'|Harga : '+str(harga)+'|Total : '+str(total)+'\n')
       i.close()
   else:
       print("Pilih menu yang tersedia")
