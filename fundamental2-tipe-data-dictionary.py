""""
TIPE DATA DICTIONARY UNTUK MENGHUBUNGKAN KEY DAN VALUE
KVP = KEY VALUE PAIR
"""

print('\nKamus Indonesia-Inggris')
kamus_ind_eng = {}
kamus_ind_eng['anak'] = 'Son'
kamus_ind_eng['istri'] = 'Wife'
kamus_ind_eng['ayah'] = 'Father'
kamus_ind_eng['ibu'] = 'Mother'

# atau
kamus_ind_eng = {'anak': 'Son', 'istri': 'Wife', 'ayah': 'Father', 'ibu': 'Mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['istri'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan informasi driver di sekitar pemakai aplikasi ')
data_dari_server_gojek = {
    'tanggal': '2021-02-14',
    'driver list': [{'nama': 'Eko', 'jarak': 10}, {'nama': 'Dwi', 'jarak': 50},{'nama': 'tri', 'jarak': 100},
                    {'nama': 'Catur', 'jarak': 1000}
                    ]
}

print(data_dari_server_gojek)
print(f"data driver sekitar sini{data_dari_server_gojek['driver list']}")
print(f"driver #1 {data_dari_server_gojek['driver list'][0]}")
print(f"driver #4 {data_dari_server_gojek['driver list'][3]}")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver list'][0]['jarak']} meter")

