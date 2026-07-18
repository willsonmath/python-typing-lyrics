"""
Project : Python Typing Lyrics
Version : 1.0
Author  : Willson Andre Simamora
Created : July 2026

Description:
Simple Python utility to create a typing effect for song lyrics.
"""
#kode untuk mempermudah membuat efek ketikan lirik lagu

import time
def ketik(teks, waktu, jeda):
    if not teks:
        print()
        time.sleep(jeda)
    else:
        speed = waktu/len(teks)
        for i in range(1,len(teks)+1):
            print(teks[:i],end="\r",flush=True)
            time.sleep(speed)
        print()
        time.sleep(jeda)

#contoh;
ketik("willson andre simamora", 5, 2)
ketik("STEI-R ITB 26", 3, 0)
#nanti tinggal ganti kata²nya jadi lirik lagu nya
#angka nya itu kan ada dua, satu untuk "berapa detik satu baris itu dinyanyikan" dan satunya lagi untuk "berapa detik jeda dari baris satu ke baris selanjutnya"

#selamat mencoba...