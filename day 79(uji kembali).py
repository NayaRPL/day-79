# panjang ,lebar,dantinggi balok berturut turut adalah, 15cm, 10cm,5cm.jika irvan ingin 
# ingin membuat 10 kerangka balok menggunakan kawat,a panjang kawat yang harus di  sediakan
# adalaha?

def ukuran():
    print('''panjang_balok=15cm
    lebar_balok=10cm 
    tinggi_balok=5cm''')
    print(''' rumus panjang kerangka balok = 4(panjang_balok*lebar_balok*tinggi balok''')
ukuran()
jumlah_kerangka_balok=int(input("masukkan kerangka balok :"))
if jumlah_kerangka_balok == 10:
    panjang_kerangka_balok=(4*(15+10+5))
    panjang_kerangka_10_balok=10*panjang_kerangka_balok
    panjang_kerangka_10_balok_satuan_meter= (panjang_kerangka_10_balok / 100)
    print("panjang kerangka balok :",panjang_kerangka_balok)  
    print("panjang kerangka 10 balok:",panjang_kerangka_10_balok)
    print("panjang_kerangka_10_balok_satuan_meter:",panjang_kerangka_10_balok_satuan_meter)
else:
    print("jumlah kerangka yanga nda masukkan bukan jumlah yang telah di ketahui dalam soal")

    