print('TIPE DATA SKALAR = Tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)


print('\nTIPE DATA LIST/DAFTAR/ARRAY')
anak = []
anak.append('Eko')
anak.append('Dwi')
anak.append('Tri')
anak.append('Catur')
print(anak)

#atau
anak = ['Eko','Dwi','Tri','Catur']
print(anak)

print('\nMenambah Anak')
anak.append('Panca')
print(anak)

print('\nsapa Anak Ke-2')
print(f'Hai {anak[1]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak Cara Lain')
for a in range(0,len(anak)):
    print(f'Hai {anak[a]}')