from logging import NullHandler


print("Tanggap Gempa")
print("------------------------------")

print("Input Untuk Lokasi :")
print("Laut = 1")
print("Pegunungan/ Daratan Tinggi = 2")
print("Daratan Rendah/ Perkotaan = 3")
print("------------------------------")

lk = int(input("Masukan Lokasi: "))
def Lokasi(lk):
    if lk == 1:
        Lokasi = 'Laut'
    elif lk == 2:
        Lokasi = 'Daratan Tinggi'
    elif lk == 3 :
        Lokasi = 'Daratan Rendah'
    else: 
        print("Tidak Tersedia")
    return Lokasi

mg = int(input('Masukkan magnitudo: '))

def magnitude(mg):
    if mg < 3:  
        statusGempa = 'Normal'
    elif mg < 4 and mg >=3:
        statusGempa = 'Waspada'
    elif mg < 6 and mg >=4:
        statusGempa = 'Siaga'
    elif mg >= 6:
        statusGempa = 'Awas'
    else:
        statusGempa = 'Tidak ada gempa'
    return statusGempa

print("Lokasi : ", Lokasi(lk))
print("Status Gempa : ", magnitude(mg))

def prediksiGP(lk, mg):
    if lk == 3 and mg < 3:
        prediksi = "Status Aman"
    elif lk == 3   and mg < 4 and mg >= 3:
        prediksi = "Status Aman"
    elif lk == 2  and mg < 3:
        prediksi = "Status Aman"
    elif lk == 2  and mg < 4 and mg >=3:
        prediksi = "Status Waspada"
    elif lk == 1 and mg < 3:
        prediksi = "Status Waspada Tsunami"
    elif lk == 3 and mg < 6 and mg >=4:
        prediksi = "Status Waspada"
    elif lk == 2 and mg <6 and mg >4:
        prediksi = "Status Siaga"
    elif lk == 3 and mg >= 6:
        prediksi = "Status Siaga"
    elif lk == 2 and mg >= 6:
        prediksi = "Status Awas Longsor"
    elif lk == 1 and mg < 6 and mg >=4:
        prediksi = "Status Waspada"
    elif lk == 1 and mg >= 6:
        prediksi = "Status Tsunami"
    else:
        prediksi = "Belum Ada Prediksi"
    return prediksi

print("Prediksi : ", prediksiGP(lk,mg))

def saranGp(lk,mg):
    if lk == 1 and mg < 3:
        saran = "aman"
    elif lk == 1 and mg >= 3 and mg < 4: 
        saran = "jauhi pantai dan sekitarnya"
    elif lk == 1 and mg >= 4 and mg < 6:
        saran = "Waspada Tsunami, Menjauh 10km dari Pantai"
    elif lk == 1 and mg >= 6:
        saran = "RUUUUUUNNNNNNNN!!!!! Panjat Pohon Kelapa!!!! Cari Tempat TINGGI!!! "
    elif lk == 2 and mg < 3:
        saran = "aman bro... ati-ati aj longsor"
    elif lk == 2 and mg >= 3 and mg < 4 :
        saran = "Hindari tebing, masuk lemari buat jaga-jaga"
    elif lk == 2 and mg >= 4 and mg < 6 :
        saran = "Longsor nih... 100% banyakin doa jangan lupa"
    elif lk == 2 and mg >= 6:
        saran = "Pasrah aja bro...,keluar rumah atau sembunyi di lemari/bawah meja. btw jangan lupa head count barangkali ada yang ilang"
    elif lk == 3 and mg < 4 :
        saran = "aman bro... lanjut goyang... "
    elif lk == 3 and mg >= 4 :
        saran = "ngumpet bro kalau gede serem ntar"
    else:
        saran = "Nothing.... Just Nothing...."
    return saran

print("Saran : ", saranGp(lk,mg))