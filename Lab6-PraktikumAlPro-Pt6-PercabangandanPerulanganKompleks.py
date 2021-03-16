#Percabangan dan Perulangan Kompleks
# Shella adalah seorang ketua kelas XI di SMA Sekolah-Sekolahan. 
# Dia diminta untuk membantu merekap nilai matematika seluruh murid di kelasnya yang berjumlah 10 orang. 
# Setelah selesai merekap nilai matematika dan menyerahkannya ke guru matematika, 
# shella tiba-tiba ingin mencoba membuat bar grafik sederhana untuk melihat perbandingan rekapannya. 
# Bantulah Shella untuk membuat bar grafik tersebut!
# Input =   Masukkan kolom yang di inginkan: 
#           Nilai baris per kolom: 
#           Judul Grafik Bar:
# Proses = For
# Output =
#=============================================================
total=0
n=int(input("Masukkan jumlah kolom yang di inginkan: "))
print("Masukkan nilai baris per kolom (range nilai: 1-10) :")
nilaikolom=[int(input())for i in range (n)]
judulbar=input("Masukkan judul grafik bar :")
judulbar=judulbar.upper()
print("\n")
print("GRAFIK BAR", judulbar)
#=============================================================
for x in range (0,n):
    if (nilaikolom[x]>total):
        total=nilaikolom[x]
for x in range (0,n):
    print("[" + str(x+1) + "]", end="")
    for y in range (0, nilaikolom[x]):
        print("*", end="")
    print()
    print()