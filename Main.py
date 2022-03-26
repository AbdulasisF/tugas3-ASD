tampungan=["Meja","Kursi"];

def tambah(): 
    print('-'*40) 
    tmb_brg = input("Masukkan barang yang akan di tambahkan :");
    tampungan.append(tmb_brg);
    print("hasil setelah di tambahkan", tampungan);
    
def hapus(): 
    print('-'*40) 
    print("List barang sekarang", tampungan);
  
    hps_brg = input('Masukkan brg yg mau di hapus:');
  
    if(hps_brg in tampungan):
      tampungan.remove(hps_brg);
      print("hasil setelah di hapus", tampungan);

def edit(): 
  print('-'*40) 

  nm_change = input("Masukkan nama barang terbaru:")
  tampungan[0] = nm_change
  print("hasil setelah di edit", tampungan)
  
def menampilkan(): 
  print('-'*40) 
  print("List semua barang")
  print('-'*40) 
  
  for i in tampungan:
    print(i)

def mengecek(): 
  print('-'*40) 
  print("List semua barang")
  print('-'*40) 
  
  for i in tampungan:
    print(i)

  cek_brg = input("Masukkan barang yang ingin diketahui:")

  if(cek_brg in tampungan):
    print("Nama barang sudah ada dalam list")
  else:
    print("Nama barang tidak ada dalam list")

def menampilkanIndex(): 
  print('-'*40) 
  brg_cek = input("Masukkan nama barang:")

  if(brg_cek in tampungan):
    for i in range(len(tampungan)):
      if(brg_cek == tampungan[i]):
        print("Index nama barang adalah", i)
  else:
    print("Nama barang tidak ada dalam list")
  
def menu(): 
 while True: 
  print('-'*40);
  print("PROGRAM BARANG".center(40,'=')) 
  print('-'*40) 
   
  print("1. Tambah Barang,");
  print("2. Hapus Barang,");
  print("3. Edit Barang,");
  print("4. Menampilkan Semua Barang,");
  print("5. Mengecek Barang,");
  print("6. Menampilkan Index Barang,");

  pilihan = int(input("Pilih menu \t:")) 

  if(pilihan == 1):
    tambah();
  elif(pilihan == 2):
    hapus()
  elif(pilihan == 3):
    edit()
  elif(pilihan == 4):
    menampilkan() 
  elif(pilihan == 5):
    mengecek()
  elif(pilihan == 6):
    menampilkanIndex()

menu();
