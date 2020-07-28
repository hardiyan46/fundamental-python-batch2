"""
Membuat Fungsi dengan contoh ksus menghitung luas segitiga
luas_segitiga = alas * tinggi /2
"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi /2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga}')

# Contoh segitiga dengan copy paste
alas = 32
tinggi = 40
luas_segitiga = alas * tinggi /2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga}')

# Contoh hitung luas segitiga dengan FUNGSI
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi /2
    return luas_segitiga
print(f'Menghitung Luas segitiga dengan Fungsi adalah {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung Luas segitiga dengan Fungsi adalah {hitung_luas_segitiga(31, 20)}')

#Contoh fungsi dengan variable alas dan tinggi
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi /2
    return luas_segitiga
alas = 10
tinggi = 35

print(f'Menghitung Luas segitiga dengan Fungsi adalah {hitung_luas_segitiga(alas, tinggi)}') #Mengambil dari nilai variabel
print(f'Menghitung Luas segitiga dengan Fungsi adalah {hitung_luas_segitiga(31, 20)}') #Nilai variabel dimasukan pada argumen