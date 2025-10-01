print("===penghitungan gaji karyawan PT.BOM===")

nama=input("masukkan nama karyawan:")
jabatan=input("masukkan jabatan karyawan:").lower()
hari_kerja=int(input("masukkan jumlah hari kerja karyawan:"))
jam_kerja=int(input("masukkan jumlah jam kerja perhari karyawan:"))
lembur=int(input("masukkan jumlah jam lembur karyawan:"))


harga_petasan=5000


if jabatan=="peracik petasan":
    if hari_kerja >=24 and jam_kerja >=8 and lembur >= 4:
        bayaran_per_jam=25000
        bayaran_lembur=15000
elif hari_kerja >=18 and jam_kerja >=6:
        bayaran_per_jam=20000
        bayaran_lembur=10000
else:
        bayaran_per_jam=15000
        bayaran_lembur=10000
    
if jabatan=="pengantar petasan":
     if hari_kerja >=20 and jam_kerja >=7 and lembur >=7:
        bayaran_per_jam=25000
        bayaran_lembur=20000
     elif hari_kerja >=16 and jam_kerja >=5 and lembur >=4:
        bayaran_per_jam=20000
        bayaran_lembur=15000
     else:
        bayaran_per_jam=15000
        bayaran_lembur=12000


total_gaji=(bayaran_per_jam*jam_kerja*hari_kerja)+(lembur*bayaran_lembur)

print("===rincian gaji===")
print("SELAMAT MENIKMATI GAJI")
print(f"nama karyawan:{nama}")
print(f"jabatan     :{jabatan}")
print(f"hari kerja   :{hari_kerja}")
print(f"jam kerja   :{jam_kerja}")
print(f"jumlah lembur:{lembur}")
print(f"bayaran per jam:RP{bayaran_per_jam}")
print(f"bayaran lembur:RP{bayaran_lembur}")
print(f"total gaji:RP{total_gaji}")
print("CAIR CAIR CAIR")

