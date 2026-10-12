print("===== Sistem Penentuan Rekomendasi Transportasi Mahasiswa ke Kampus =====")
#Input Jarak
jarak = float(input("Masukkan jarak rumah ke kampus (km): "))

#IF : Menampilkan pesan jika jarak memenuhi syarat
if jarak > 0 and jarak <= 15:
    print("Jarak berhasil dimasukkan.")

#IF - ELSE : Menentukan kevalidan suatu jarak
status_jarak = "tidak valid"

if jarak > 0 and jarak <= 15:
    print("Jarak valid.")
    status_jarak = "valid"

else:
    print("Jarak tidak valid!")
    print("Silahkan memulai kembali program dan masukkan input yang benar!")
    print("Program Berakhir.")
    raise SystemExit

#IF - ELIF - ELSE : Mengelompokkan jarak berdasarkan rentang km
if jarak <= 0.5:
    kategori = "Sangat dekat."
elif jarak <= 1:
    kategori = "Dekat."
elif jarak <= 3:
    kategori = "Menengah."
elif jarak <= 5:
    kategori = "Sedang."
elif jarak <= 10:
    kategori = "Jauh."
else:
    kategori = "Sangat jauh."

#Variabel rekomendasi dan biaya
transportasi = ""
biaya = 0

#Validasi cuaca
while True:
    cuaca = input("Masukkan cuaca saat ini (cerah/mendung/hujan): ").lower()
    if cuaca in ("cerah", "mendung", "hujan"):
        print("Cuaca valid.")
        break
    else:
        print("Cuaca tidak valid. Input ulang!")

#Validasi kendaraan
while True:
    kendaraan = input("Apakah kamu memiliki kendaraan? (motor/mobil/tidak): ").lower()
    if kendaraan in ("motor", "mobil", "tidak"):
        print("Kendaraan valid.")
        break
    else:
        print("Kendaraan tidak valid. Input ulang!")

while True:
    sepeda = input("Apakah kamu memiliki sepeda? (ya/tidak): ").lower()
    if sepeda in ("ya", "tidak"):
        print("Sepeda valid.")
        break
    else:
        print("Sepeda tidak valid. Input ulang!")

while True:
    angkot = input("Apakah di daerahmu ada angkot? (ya/tidak): ").lower()
    if angkot in ("ya", "tidak"):
        print("Angkot valid.")
        break
    else:
        print("Angkot tidak valid. Input ulang!")

while True:
    budget = float(input("Masukkan budget transportasi (Rp0 - Rp1jt): "))
    if budget >= 0 and budget <= 1000000:
        print("Budget valid.")
        break
    else:
        print("Budget tidak valid. Input ulang!")

#IF - ELIF - ELSE : Menentukan rekomendasi transportasi dan biaya
#<=1 KM dan Hujan
if jarak <= 1:

    if cuaca == "hujan" :
        if jarak <= 0.2:
            transportasi = "Jalan kaki"
            biaya = 0
        elif kendaraan == "motor":
            transportasi = "Motor pribadi"
            biaya = jarak * 2000
        elif kendaraan == "mobil":
            transportasi = "Mobil pribadi"
            biaya = jarak * 4000
        elif angkot == "ya":
            transportasi = "Angkutan umum"
            biaya = jarak * 3000
        else:
            transportasi = "Ojek online"
            biaya = jarak * 4000

#<=1 dan Tidak Hujan
    else:

        if jarak <= 0.5:
            transportasi = "Jalan kaki"
            biaya = 0
        elif sepeda == "ya":
            transportasi = "Sepeda"
            biaya = 0
        elif kendaraan == "motor":
            transportasi = "Motor pribadi"
            biaya = jarak * 2000
        elif kendaraan == "mobil":
            transportasi = "Mobil pribadi"
            biaya = jarak * 4000
        elif angkot == "ya":
            transportasi = "Angkutan umum"
            biaya = jarak * 3000
        else: 
            transportasi = "Ojek online"
            biaya = jarak * 4000

#> 1KM dan <= 10KM
elif jarak <= 10:

    if kendaraan == "motor":
        transportasi = "Motor pribadi"
        biaya = jarak* 2000
    elif kendaraan == "mobil":
        transportasi = "Mobil pribadi"
        biaya = jarak * 4000
    elif angkot == "ya":
        transportasi = "Angkutan umum"
        biaya = jarak * 3000
    else:
        transportasi = "Ojek online"
        biaya = jarak * 4000

#> 10 KM dan <= 15KM
else:

    if kendaraan == "motor":
        transportasi = "Motor pribadi"
        biaya = jarak* 2000
    elif kendaraan == "mobil":
        transportasi = "Mobil pribadi"
        biaya = jarak * 4000
    else:
        transportasi = "Ojek online"
        biaya = jarak * 4000

#Periksa budget >= biaya
if budget >= biaya:
    print("\n=== Hasil Rekomendasi ===")
    print(f"Kategori jarak : {kategori}")
    print(f"Rekomendasi    : {transportasi}")
    print(f"Estimasi biaya : Rp{biaya:,.0f}")
else:
    print("\nBudget tidak cukup untuk transportasi yang direkomendasikan!")

    rekomendasi_awal = transportasi
    alternatif = "tidak ada"
    biaya_alternatif = 0

    #Mencari alternatif jalan kaki
    if alternatif == "tidak ada" and transportasi != "jalan kaki":
        if (cuaca == "hujan" and jarak <= 0.2) or (cuaca != "hujan" and jarak <= 0.5):
            alternatif = "Jalan kaki"
            biaya_alternatif = 0

    #Mencari alternatif sepeda
    if alternatif == "tidak ada" and sepeda == "ya" and transportasi != "Sepeda":
        alternatif = "Sepeda"
        biaya_alternatif = 0

    #Mencari alternatif motor
    if alternatif == "tidak ada" and kendaraan == "motor" and transportasi != "Motor pribadi" and budget >= jarak * 2000:
        alternatif = "Motor pribadi"
        biaya_alternatif = jarak * 2000

    #Mencari alternatif mobil
    if alternatif == "tidak ada" and kendaraan == "mobil" and transportasi != "Mobil pribadi" and budget >= jarak * 4000:
        alternatif = "Mobil pribadi"
        biaya_alternatif = jarak * 4000

    #Mencari alternatif motor
    if alternatif == "tidak ada" and angkot == "ya" and transportasi != "Angkutan umum" and budget >= jarak * 3000:
        alternatif = "Angkutan umum"
        biaya_alternatif = jarak * 3000

    #Mencari alternatif ojek online
    if alternatif == "tidak ada" and transportasi != "Ojek online" and budget >= jarak * 4000:
        alternatif = "Ojek online"
        biaya_alternatif = jarak * 4000

    #Menampilkan hasil alternatif
    if alternatif != "tidak ada":
        print(f"Rekomendasi awal : {rekomendasi_awal}")
        print(f"Alternatif       : {alternatif}")
        print(f"Estimasi biaya   : Rp{biaya_alternatif:,.0f}")
    else:
        print("Mohon maaf, budget tidak mencukupi untuk alternatif transportasi yang tersedia! Nebeng teman aja sudah.")
        print("Kalo gabisa nebeng teman berdoa aja sudah T-T")

print("Program Berakhir.")
