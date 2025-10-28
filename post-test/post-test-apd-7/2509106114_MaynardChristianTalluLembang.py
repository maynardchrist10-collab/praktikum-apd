
data_ban = {
    1: {"motor": "Nmax", "merek": "Michelin", "ukuran": "110/70-13", "harga": 450000},
    2: {"motor": "Nmax", "merek": "Maxxis", "ukuran": "130/70-13", "harga": 430000},
    3: {"motor": "Nmax", "merek": "IRC", "ukuran": "110/70-13", "harga": 350000},
    4: {"motor": "Nmax", "merek": "Dunlop", "ukuran": "130/70-13", "harga": 420000},
    5: {"motor": "Supermoto", "merek": "Pirelli", "ukuran": "120/70-17", "harga": 1500000},
    6: {"motor": "Supermoto", "merek": "Metzeler", "ukuran": "160/60-17", "harga": 1650000},
    7: {"motor": "Vario", "merek": "FDR", "ukuran": "80/90-14", "harga": 180000},
    8: {"motor": "Vario", "merek": "IRC", "ukuran": "90/90-14", "harga": 200000},
    9: {"motor": "Xmax", "merek": "Michelin", "ukuran": "120/70-15", "harga": 750000},
    10: {"motor": "Xmax", "merek": "Bridgestone", "ukuran": "140/70-14", "harga": 780000},
    11: {"motor": "Beat", "merek": "FDR", "ukuran": "80/90-14", "harga": 170000},
    12: {"motor": "Beat", "merek": "IRC", "ukuran": "90/80-14", "harga": 190000},
    13: {"motor": "MX", "merek": "Dunlop", "ukuran": "70/90-17", "harga": 250000},
    14: {"motor": "MX", "merek": "IRC", "ukuran": "80/90-17", "harga": 230000},
    15: {"motor": "Scoopy", "merek": "FDR", "ukuran": "90/90-12", "harga": 200000},
    16: {"motor": "Scoopy", "merek": "IRC", "ukuran": "100/90-12", "harga": 210000}
}

toko_nama = "Toko Ban "
admin = "REJA"
jalan = True



def tampilkan_data():
    """Menampilkan seluruh data ban."""
    print(f"== DATA BAN DI {toko_nama} ==")
    if not data_ban:
        print("Tidak ada data ban.")
    else:
        for id_ban, info in data_ban.items():
            print(f"ID: {id_ban} | Motor: {info['motor']} | "
                  f"Merek: {info['merek']} | Ukuran: {info['ukuran']} | "
                  f"Harga: Rp{info['harga']:,}")



def cari_ban_berdasarkan_motor(motor_cari):
    """Mencari data ban berdasarkan jenis motor."""
    ditemukan = False
    for id_ban, info in data_ban.items():
        if info['motor'].lower() == motor_cari.lower():
            print(f"ID: {id_ban} | Merek: {info['merek']} | Ukuran: {info['ukuran']} | Harga: Rp{info['harga']:,}")
            ditemukan = True
    if not ditemukan:
        print("Ban untuk motor tersebut tidak ditemukan.")



def tambah_data():
    """Menambah data ban baru ke dalam dictionary."""
    print("=== TAMBAH DATA BAN ===")
    try:
        id_baru = max(data_ban.keys()) + 1 if data_ban else 1
        motor = input("Masukkan jenis motor: ")
        merek = input("Masukkan merek ban: ")
        ukuran = input("Masukkan ukuran ban: ")
        harga = int(input("Masukkan harga ban: "))

        # variabel lokal: id_baru, motor, merek, ukuran, harga
        data_ban[id_baru] = {"motor": motor, "merek": merek, "ukuran": ukuran, "harga": harga}
        print(" Data berhasil ditambahkan!")
    except ValueError:
        print(" Input harga harus berupa angka!")



def ubah_data(id_edit):
    """Mengubah data ban berdasarkan ID."""
    try:
        if id_edit in data_ban:
            motor = input("Masukkan jenis motor baru: ")
            merek = input("Masukkan merek baru: ")
            ukuran = input("Masukkan ukuran baru: ")
            harga = int(input("Masukkan harga baru: "))

            data_ban[id_edit] = {"motor": motor, "merek": merek, "ukuran": ukuran, "harga": harga}
            print(" Data berhasil diubah!")
        else:
            print(" ID tidak ditemukan!")
    except ValueError:
        print(" Input harga harus berupa angka!")



while jalan:
    print(f"=== MENU {toko_nama.upper()} ===")
    print("1. Tampilkan Data Ban")
    print("2. Tambah Data Ban")
    print("3. Ubah Data Ban")
    print("4. Hapus Data Ban")
    print("5. Cari Ban Berdasarkan Motor")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    
    if pilihan == "1":
        tampilkan_data()

    
    elif pilihan == "2":
        tambah_data()

   
    elif pilihan == "3":
        tampilkan_data()
        try:
            id_edit = int(input("Masukkan ID ban yang ingin diubah: "))
            ubah_data(id_edit)
        except ValueError:
            print(" Input ID harus berupa angka!")

    
    elif pilihan == "4":
        tampilkan_data()
        try:
            id_hapus = int(input("Masukkan ID ban yang ingin dihapus: "))
            if id_hapus in data_ban:
                del data_ban[id_hapus]
                print(" Data berhasil dihapus!")
            else:
                print(" ID tidak ditemukan!")
        except ValueError:
            print(" Input ID harus berupa angka!")

    
    elif pilihan == "5":
        motor_cari = input("Masukkan jenis motor yang ingin dicari: ")
        cari_ban_berdasarkan_motor(motor_cari)

    
    elif pilihan == "6":
        print(f"Terima kasih telah berbelanja di {toko_nama}. Sampai jumpa, {admin}!")
        jalan = False

    else:
        print(" Pilihan tidak valid, silakan coba lagi.")
