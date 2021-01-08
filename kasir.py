#Fungsi tag print adalah untuk mencetak text
print('===========Ingin makan apa hari ini============')

#lalu kita tulis library / array dari variable menu
menu = {'Ayam goreng':10000,'Bakso':9000,'Mie Goreng':3000,'Ikan bakar':20000,'Sate':8000}
# setelah itu kita buat looping mengunakan for
for i in menu:
    print(i+':'+str(menu[i]))
#Jika sudah lanjut membuat input untuk memasukan pernyataan
print('===========================================')
makan = input('Makanan apa yg ingin di beli :')
jumlah = int(input('Masukan jumlah maknan :'))
uang = int(input('Masukan jumlah uang yg akan di bayar :'))

'''setelah itu kita masukan if statement
Jika variabel makan memasukan input 'Ayam goreng' 
maka nilai variabel harga sama dengan libbrary dengan kata kunci 'Ayam goreng'
begitupun seterusnya
'''
if makan == 'Ayam goreng':
    harga = menu['Ayam goreng']
elif makan == 'Bakso':
    harga = menu['Bakso']
elif makan == 'Mie Goreng':
    harga = menu['Mie Goreng']
elif makan == 'Ikan bakar':
    harga = menu['Ikan bakar']
elif makan == 'Sate':
    harga = menu['Sate']
#Jika semua kondisi tidak terpenuhi maka cetak !!!Masukan nama makanan yg sesuai di menu
else:
    print('!!!Masukan nama makanan yg sesuai di menu')
#Lalu kita kasih variabel total untuk menghitung keseluruhan total belanja
total = harga*jumlah
#Lalu kita kasih variabel kembalian untuk menghitung jumlah kembalian dari uang yg kita punya
kembalian = total - uang

#Jika uang lebih kecil dari total maka cetak: uang anda kurang
if uang < total:
    print ('Uang anda kurang')
#jika kondisi di atas tidak terpenuhi
else:
    print('============================================')
    print('Makanan yg di beli :'+makan)
    print('Jumlah yang dibeli :'+str(jumlah))
    print('SUB TOTAL          :'+str(total))
    print('Uang yg di bayar   :'+str(uang))
    print('Kembalian          :'+str(kembalian))
    print('============================================')




