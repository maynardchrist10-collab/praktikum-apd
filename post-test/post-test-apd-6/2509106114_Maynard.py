# Program pakai dictionary


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

jalan = True

while jalan:
    print("\n=== MENU TOKO BAN ===")
    print("1. Tampilkan Data Ban")
    print("2. Tambah Data Ban")
    print("3. Ubah Data Ban")
    print("4. Hapus Data Ban")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    # READ
    if pilihan == "1":
        print("\n=== DATA BAN TOKO ===")
        if not data_ban:
            print("Tidak ada data ban.")
        else:
            for id_ban, info in data_ban.items():
                print(f"ID: {id_ban} | Motor: {info['motor']} | "
                      f"Merek: {info['merek']} | Ukuran: {info['ukuran']} | "
                      f"Harga: Rp{info['harga']:,}")

    # CREATE
    elif pilihan == "2":
        print("\n=== TAMBAH DATA BAN ===")
        id_baru = max(data_ban.keys()) + 1 if data_ban else 1
        motor = input("Masukkan jenis motor: ")
        merek = input("Masukkan merek ban: ")
        ukuran = input("Masukkan ukuran ban: ")
        harga = int(input("Masukkan harga ban: "))
        data_ban[id_baru] = {"motor": motor, "merek": merek, "ukuran": ukuran, "harga": harga}
        print("Data berhasil ditambahkan!")

    # UPDATE
    elif pilihan == "3":
        print("\n=== UBAH DATA BAN ===")
        for id_ban, info in data_ban.items():
            print(f"ID: {id_ban} | Motor: {info['motor']} | Merek: {info['merek']}")
        try:
            id_edit = int(input("Masukkan ID ban yang ingin diubah: "))
            if id_edit in data_ban:
                motor = input("Jenis motor baru: ")
                merek = input("Merek baru: ")
                ukuran = input("Ukuran baru: ")
                harga = int(input("Harga baru: "))
                data_ban[id_edit] = {"motor": motor, "merek": merek, "ukuran": ukuran, "harga": harga}
                print("Data berhasil diubah!")
            else:
                print("ID tidak ditemukan!")
        except ValueError:
            print("Input ID harus berupa angka!")

    # DELETE
    elif pilihan == "4":
        print("=== HAPUS DATA BAN ===")
        for id_ban, info in data_ban.items():
            print(f"ID: {id_ban} | Motor: {info['motor']} | Merek: {info['merek']}")
        try:
            id_hapus = int(input("Masukkan ID ban yang ingin dihapus: "))
            if id_hapus in data_ban:
                del data_ban[id_hapus]
                print("Data berhasil dihapus!")
            else:
                print("ID tidak ditemukan!")
        except ValueError:
            print("Input ID harus berupa angka!")

    # EXIT
    elif pilihan == "5":
        print("Terima kasih telah membeli di toko kami.")
        jalan = False

    else:
        print("Pilihan tidak valid, coba lagi.")
