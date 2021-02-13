# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL : Eksekusi Berurutan


print('Hello World!')
print('by. Ebe')
print('Tanggal 14 Februari 2021')
print('--' * 10)

# PERCABANGAN : Eksekusi Terpilih
ingin_cepat = False
if ingin_cepat:
    print('Ambil jalan memutar')
else:
    print('Jalan lurus saja ya')


#PERULANGAN
jumlah_anak = 4
print('Halo Anak ke-1')
print('Halo Anak ke-2')
print('Halo Anak ke-3')
print('Halo Anak ke-4')
#atau
for index_anak in range(1,jumlah_anak+1):#jumlah perulangan 5 - 1 = 4
    print(f'Halo Anak ke-{index_anak}')