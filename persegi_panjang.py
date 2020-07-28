"""
Contoh menghitung Luas persegi panjang P*L*T
"""
#panjang = 10
#lebar = 15
#tinggi = 7
luas_persegi_panjang = panjang * lebar * tinggi
print(f'Luas persegi panjang dengan panjang {panjang}, lebar {lebar}dan tinggi {tinggi} adalah {luas_persegi_panjang}')

"""
Contoh mebuat fungsi hiung luas persegi panjang
"""

def hitung_luas_persegi_panjang (panjang, lebar, tinggi):
    luas_persegi_panjang = panjang * lebar * tinggi
    return luas_persegi_panjang

print(f'Luas Persegi panjang dengan FUNGSI {hitung_luas_persegi_panjang(panjang, lebar, tinggi)}')