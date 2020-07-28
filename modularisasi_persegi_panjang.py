"""
Contoh menghitung Luas persegi panjang P*L*T
"""
panjang = 10
lebar = 15
luas_persegi_panjang = panjang * lebar
print(f'Luas persegi panjang dengan panjang {panjang}, lebar {lebar} adalah {luas_persegi_panjang}')

"""
Contoh mebuat fungsi hiung luas persegi panjang
"""
def hitung_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

print(f'Luas Persegi panjang dengan FUNGSI {hitung_luas_persegi_panjang(panjang, lebar)}')