# program python2 boss
# program fungsi sederhana boss 
# di ciptakannya program ini hanya untuk belajar semata
# dan untuk di olah menjadi lebih baik dan lebih bagus lagi kawan
# https://github.com/subhanfadilah

import os, sys
os.system('clear')

# contoh fungsi 
def anakayam():
	print('harga 1 anak ayam Rp. 2.000')

def hargaanakayam(kg):
	anakayam()
	harga = 2000
	totalharga = kg*harga
	print 'harga',kg,'anak ayam adalah Rp.',totalharga
hargaanakayam(10) # di dalam kurung isi dengan angka, apabila tidak di isi dengan angka maka program akan error

peringatan = raw_input('[?] Apakah ingin mengulang program [y/n] : ')
if peringatan == 'y':
	os.system('python2 fungsi.py')
elif peringatan == 't':
	exit()
else:
	print ('system program error boss :(')





