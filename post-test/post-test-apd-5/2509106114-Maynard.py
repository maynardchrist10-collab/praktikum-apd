# Program CRUD Toko Ban


data_ban = [
    (1, "Nmax", "Michelin", "110/70-13", 450000),
    (2, "Nmax", "Maxxis", "130/70-13", 430000),
    (3, "Nmax", "IRC", "110/70-13", 350000),
    (4, "Nmax", "Dunlop", "130/70-13", 420000),
    (5, "Supermoto", "Pirelli", "120/70-17", 1500000),
    (6, "Supermoto", "Metzeler", "160/60-17", 1650000),
    (7, "Vario", "FDR", "80/90-14", 180000),
    (8, "Vario", "IRC", "90/90-14", 200000),
    (9, "Xmax", "Michelin", "120/70-15", 750000),
    (10, "Xmax", "Bridgestone", "140/70-14", 780000),
    (11, "Beat", "FDR", "80/90-14", 170000),
    (12, "Beat", "IRC", "90/80-14", 190000),
    (13, "MX", "Dunlop", "70/90-17", 250000),
    (14, "MX", "IRC", "80/90-17", 230000),
    (15, "Scoopy", "FDR", "90/90-12", 200000),
    (16, "Scoopy", "IRC", "100/90-12", 210000)
]


jalan = True

while jalan:
    print("=== MENU TOKO BAN ===")
    print("1. Tampilkan Data Ban")
    print("2. Tambah Data Ban")
    print("3. Ubah Data Ban")
    print("4. Hapus Data Ban")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    # READ
    if pilihan == "1":
        print("=== DATA BAN TOKO ===")
        if not data_ban:
            print("Tidak ada data ban.")
        else:
            for ban in data_ban:
                print(f"ID: {ban[0]} | Motor: {ban[1]} | Merek: {ban[2]} | Ukuran: {ban[3]} | Harga: Rp{ban[4]:,}")

    # CREATE
    elif pilihan == "2":
        print("=== TAMBAH DATA BAN ===")
        id_baru = len(data_ban) + 1
        motor = input("Masukkan jenis motor: ")
        merek = input("Masukkan merek ban: ")
        ukuran = input("Masukkan ukuran ban: ")
        harga = int(input("Masukkan harga ban: "))
        data_ban.append((id_baru, motor, merek, ukuran, harga))
        print("Data berhasil ditambahkan!")

    # UPDATE
    elif pilihan == "3":
        print("=== UBAH DATA BAN ===")
        for ban in data_ban:
            print(f"ID: {ban[0]} | Motor: {ban[1]} | Merek: {ban[2]}")
        id_edit = int(input("Masukkan ID ban yang ingin diubah: "))

        ditemukan = False
        for i in range(len(data_ban)):
            if data_ban[i][0] == id_edit:
                motor = input("Jenis motor baru: ")
                merek = input("Merek baru: ")
                ukuran = input("Ukuran baru: ")
                harga = int(input("Harga baru: "))
                data_ban[i] = (id_edit, motor, merek, ukuran, harga)
                print("✅Data berhasil diubah!")
                ditemukan = True
        if not ditemukan:
            print(" ID tidak ditemukan!")

    # DELETE
    elif pilihan == "4":
        print("=== HAPUS DATA BAN ===")
        for ban in data_ban:
            print(f"ID: {ban[0]} | Motor: {ban[1]} | Merek: {ban[2]}")
        id_hapus = int(input("Masukkan ID ban yang ingin dihapus: "))
        ditemukan = False
        for ban in data_ban:
            if ban[0] == id_hapus:
                data_ban.remove(ban)
                print(" Data berhasil dihapus!")
                ditemukan = True
                break
        if not ditemukan:
            print(" Data tidak ditemukan!")

    # EXIT
    elif pilihan == "5":
        print(" Terima kasih telah membeli di toko kami.")
        jalan = False  # ubah variabel menjadi False untuk menghentikan loop

    else:
        print("Pilihan tidak valid.")