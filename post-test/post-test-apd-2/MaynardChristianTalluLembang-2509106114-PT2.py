#perhitungan biaya bahan bangunan

nama=input("nama pelanggan:")
jumlah_batu_bata=int(input("jumlah batu bata yang mau di beli:"))
jumlah_semen=int(input("jumlah semen yang mau dibeli:"))


harga_batu_bata=100
harga_semen=100000

total_awal=(jumlah_batu_bata*harga_batu_bata)+(jumlah_semen*harga_semen)

paket_hemat=(jumlah_batu_bata==500 and jumlah_semen==5)
paket_ultra_mantap=(jumlah_batu_bata==2000 and jumlah_semen==16)

diskon=0.0
keterangan_diskon="tidak ada diskon"

if paket_hemat:
    diskon=0.15
    keterangan_diskon="paket hemat(15%)"
elif paket_ultra_mantap:
    diskon=0.30
    keterangan_diskon="paket ultra mantap(30%)"

jumlah_diskon=total_awal*diskon 
total_akhir=total_awal-jumlah_diskon


#output
print("struk biaya bahan bangunan")
print(f"nama pelanggan:{nama}")
print(f"|{jumlah_batu_bata:<10}|{jumlah_batu_bata:<7}|{harga_batu_bata:<13}|")
print(f"|{jumlah_semen:<10}|{jumlah_semen:<7}|Rp{harga_semen:<12}|")
print(f"Total Biaya Awal : Rp{total_awal:,.0f}")
print(f"Diskon           : {keterangan_diskon}")
print(f"total biaya awal:Rp{total_awal:,.0f}")
print(f"total biaya akhir :Rp{total_akhir:,.0f}") 