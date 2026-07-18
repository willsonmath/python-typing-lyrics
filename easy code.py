"""
Project : Python Typing Lyrics
Version : 1.0
Author  : Willson Andre Simamora
Created : July 2026

Description:
Simple Python utility to create a typing effect for song lyrics.
"""
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

#Example;
ketik("willson andre simamora", 5, 2)
ketik("STEI-R ITB 26", 3, 0)
