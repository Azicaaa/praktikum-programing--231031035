print('Tugas Praktikum 4'.center(35))
nama = 'Nama Mahasiswa'
nim  = 'nim-mahasiswa'
prodi= 'Sistem Informasi B'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
#output: dfv neumann

str3 = 'duFort Frankel Von Neumann'
#output: DUFORT F V N

str4 = 'duFOrt Frankel Von Neumann'
#output: N duFort f v

str5 = 'DuFort Frankel Von Neumann'
#output: NEUMANN d f v

str6 = 'duFort Frankel Von Neumann'
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
#output: duFort Frankel Von NEUMANN

str8 = '#duFort@Frankel@Von@Neumann$'
#output: duFort Frankel Von Neumann

str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
#output: duFort Frankel Von Neumann

str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
#output: duFort Frankel Von Neumann