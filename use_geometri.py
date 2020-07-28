#Contoh 1
from geometri.persegi_panjang import hitung_luas_persegi_panjang  #contoh import fungsi hitung luas persegi panjang
from geometri.segitiga import hitung_luas_segitiga  #contoh import fungsi hitung luas segitiga pada contoh2

panjang = 30
lebar = 30
print(f'Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {hitung_luas_persegi_panjang(panjang,lebar)}')


#Contoh 2
alas = 20
tinggi = 10
print(f'Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {hitung_luas_segitiga(alas, tinggi)}')