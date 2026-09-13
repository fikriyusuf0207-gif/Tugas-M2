#no 1 
TotalBarang=1250
SlotKardus=45
Kardus_penuh=TotalBarang/SlotKardus
print('Kardus Penuh:',int(Kardus_penuh))
sisa=TotalBarang%SlotKardus
print('sisa:',sisa)
#no 2
sp=85
sl=70
Nilai_akhir=sp*0.6+sl*0.4
print("Nilai akhir:",Nilai_akhir)
#no 3
BP=50000
KT=1000
BS=400
EOQ=((2*BP*KT)/BS)**0.5
print("Nilai EOQ:",EOQ)
#no 4
kata1= "Statistika"
kata2= "Bisnis"
kata3= "ITS"
print(kata1+" "+kata2+" "+kata3)
#no 5
departemen="Statistika Bisnis"
print("Jawaban No.5:", departemen[:1], departemen[-1:])
#no 6
matkul='Analisis Data Eksploratif'
print("Jawaban no.6:",matkul[9:14:1])
#no 7
nama_matkul='aLgoRitmA pEmroGramAn'
print('Jawaban no.7:', nama_matkul.title())
#no 8
teks="Mahasiswa DSB Kelas 1C sangat senang belajar AlPROG"
print('No.8 jumlah karakter:',len(teks))
print("No.8 jumlah karakter'a':",teks.count("a"))
#no 9
p=100
l=4
Jumlah_kolom= p//l
karakter='='
print("No.9 Jumlah kolom yang muat adalah ",Jumlah_kolom)
print("karakter'='no.9:", karakter*Jumlah_kolom)
#no 10
a= 50000
b= 35000
pesan= "Sisa saldo Anda adalah Rp"
c=a-b
print('No.10',pesan+str(c))