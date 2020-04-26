# program python2 boss
# program tebak sederhana boss 
# di ciptakannya program ini hanya untuk belajar semata
# dan untuk di olah menjadi lebih baik dan lebih bagus lagi kawan
# https://github.com/subhanfadilah

import os 
import sys
os.system('clear')

jawaban = raw_input('Apakah anda manusia : ') # ini adalah sebuah variabel bernama jawaban
if jawaban == 'ya': # ini adalah sebuah bentuk percabangan if
	print "==> selamat anda mendapatkan hadiah uang tunai sebesar 10m" # apabila jawaban benar maka yang di outputkan adalah kalimat baris ini
else:
	print "[X] salah boyy" # dan apabila jawaban salah maka yang di outputkan adalah kalimat baris ini
