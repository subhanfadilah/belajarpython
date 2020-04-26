# program python boss
# program teks berjalan sederhana boss 
# di ciptakannya program ini hanya untuk belajar semata
# dan untuk di olah menjadi lebih baik dan lebih bagus lagi kawan
# https://github.com/subhanfadilah

import os 
import sys
import time

os.system('clear')

# ini adalah fungsi 
def jalan (kata):
	for c in kata:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)
jalan('Diciptakannya porgram ini hanya untuk belajar semata ya gan '.center(5)) # ini adalah output program teks berjalan
jalan('dan untuk di kembangkan supaya kita semua bisa belajar dari program sederhana ini dan merubahnya menjadi program luar biasa ....'.center(5)) # ini adalah output program teks berjalan
time.sleep(5)
os.system('clear')

