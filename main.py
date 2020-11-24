bahan = []
jumlah = []
harga = []
 
def tampil_bahan():
   if len(bahan) <= 0:
       print ("BAHAN KOSONG")
   else:
       print("ID     Nama Bahan     Jumlah Bahan     Harga Bahan")
       print("--------------------------------------------------------")
       for i in range(len(bahan)):
           print(i+1,"    ",bahan[i],"         ",jumlah[i],"          ",harga[i])
 
 
def tambah_bahan():
   nama_bahan = input("Nama Bahan: ")
   bahan.append(nama_bahan)
   jumlah_bahan = input("Jumlah Bahan: ")
   jumlah.append(jumlah_bahan)
   harga_bahan = input("Harga Bahan: ")
   harga.append(harga_bahan)
 
def ubah_bahan():
   tampil_bahan()
   i = int(input("Inputkan ID bahan: "))
   if(i>len(bahan)):
       print ("Bahan tidak ditemukan")
   else:
       nama_bahan = input("Nama Bahan: ")
       bahan[i] = nama_bahan
 
def hapus_bahan():
   tampil_bahan()
   i = int(input("Inputkan ID buku: "))
   if(i>len(bahan)):
       print("ID Salah")
   else:
       bahan.remove(bahan[i])
       jumlah.remove(jumlah[i])
       harga.remove(harga[i])
 
def tampil_menu():
   print("\n")
   print("-------MENU-------".center(55))
   print("")
   print("[1]Tampil    [2]Tambah   [3]Ubah    [4]Hapus   [5]Keluar")
   print("")
 
   menu = int(input("PILIH MENU: "))
   print("\n")
 
   if menu == 1:
       tampil_bahan()
   elif menu == 2:
       tambah_bahan()
   elif menu == 3:
       ubah_bahan()
   elif menu == 4:
       hapus_bahan()
   elif menu == 5:
       exit()
   else:
       print ("Salah Pilih")
 
if __name__=="__main__":
   while(True):
       tampil_menu()
