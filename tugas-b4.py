print('Tugas Praktikum 4'.center(35))
nama = 'Siti nur azizah'
nim  = '231031035'
prodi= 'Sistem Informasi B'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''
print('\n'*2)


print('----------STR1---------')
str1 = 'duFort Frankel Von Neumann'
a = str1.upper()
a = a.split()
print(a[-1],a[0],a[1],a[2])
#output: NEUMANN DUFORT FRANKEL VON

print()

print('----------STR2---------')
str2 = 'duFort Frankel Von Neumann'
a = str2.lower()
a = a.split()
print(a[0][0]+a[0][2]+a[2][0],a[-1])
#output: dfv neumann

print()

print('----------STR3---------')
str3 = 'duFort Frankel Von Neumann'
a = str3.upper()
a = a.split()
print(a[0],a[1][0],a[2][0],a[-1][0])
#output: DUFORT F V N

print()

print('----------STR4---------')
str4 = 'duFOrt Frankel Von Neumann'
a = str4.upper()
a = a.split()
print(a[-1][-1].upper(),a[0][0:2].lower()+a[0][2:3]+a[0][3].lower()+a[0][4:6].lower(),a[1][0].lower(),a[2][0].lower())
#output: N duFort f v

print()

print('----------STR5---------')
str5 = 'DuFort Frankel Von Neumann'
a = str5.upper()
a = a.split()
print(a[-1],a[0][0].lower(),a[1][0].lower(),a[2][0].lower())
#output: NEUMANN d f v

print()

print('----------STR6---------')
str6 = 'duFort Frankel Von Neumann'
a = str6.upper()
a = a.split()
print(a[-1],a[0][0]+a[1][0]+a[2][0])
#output: NEUMANN DFV

print()

print('----------STR7---------')
str7 = '@duFort Frankel Von Neumann$'
a = str7.split()
print(a[0].strip('@'),a[1],a[2],a[-1][0:6].strip('$').upper())
#output: duFort Frankel Von NEUMAN

print()

print('----------STR8---------')
str8 = '#duFort@Frankel@Von@Neumann$'
a = str8.replace('@',' ')
print(a.strip('#$'))
#output: duFort Frankel Von Neumann

print()

print('----------STR9---------')
str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
a = (str9.replace('@#^',' ').replace('*#(',' ').replace('(#(',' '))
print(a.strip('@$'))
#output: duFort Frankel Von Neumann

print()

print
print('----------STR10---------')
str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
a = (str10.replace('@!^',' ').replace('!1(',' ').replace('(!(',' '))
b = a.strip('@^')
b = b.split()
print(b[0][0:3].lower()+b[0][3:6].lower(),b[1].capitalize(),b[2].capitalize(),b[3].capitalize())
#output: duFort Frankel Von Neumann