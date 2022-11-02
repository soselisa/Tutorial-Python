import random

angkaRahasia = random.randint(1,20)
print('Tebak angka dari angka 1 s/d 20')
 
for tebakan in range(1, 7):
    tebak = int(input('Masukkan angka tebakan: '))
    if tebak < angkaRahasia :
        print('Terlalu rendah.')
    elif tebak > angkaRahasia :
        print('Terlalu tinggi.')
    else:
        break

if tebak == angkaRahasia:
    print(f'Selamat! kamu berhasil menebak angka di tebakan ke-{tebakan}')
else:
    print(f'Salah! Angka yang saya pikirkan adalah {angkaRahasia}')