print('praktikum-3\n\n')
print('NAMA : SITI NUR AZIZAH IBRAHIM')
print('NIM  : 231031035')
print('prodi: Sistem Informasi B\n')

##########################################

a = True
b = False

print('\n============NAND============')
hasil = not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil = not (a and b)
print(a,'nand',b'adalah =',hasil)
hasil = not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil = not (b and b)
print(b,'nand',b,'adalah =',hasil)

print('\n============NOR============')
hasil = not (a or a)
print(a,'nor',a,'adalah =',hasil)
hasil = not (a or b)
print(a,'nor',b'adalah =',hasil)
hasil = not (b or a)
print(b,'nor',a,' adalah =',hasil)
hasil = not (b or b)
print(b,'nor',b,' adalah =',hasil)

print('\n============NXOR============')
hasil = not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil = not (a ^ b)
print(a,'nxor',b'adalah =',hasil)
hasil = not (b ^ a)
print(b,'nxor',a,' adalah =',hasil)
hasil = not (b ^ b)
print(b,'nxor',b,' adalah =',hasil)

# INI OPERATOR MEMBERSHIP
print('\n============ IN ============')
nama =('Siti Nur Azizah Ibrahim')

test = 'ti'
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test = 'it'
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'ada di',nama,'adalah=',cek)

cek = test2 in nama
print(test2,'ada di',nama,'adalah=',cek)

cek = test3 in nama
print(test3,'ada di',nama,'adalah=',cek)

cek = test4 in nama
print(test4,'ada di',nama,'adalah=',cek)

cek = test5 in nama
print(test5,'ada di',nama,'adalah=',cek)

# INI operator BITWISE
print('\n')
a = 25
b = 4
a += 60
b += 80
print('========AND========')
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',b,'biner adalah=',format(b,'09b'))
print('---------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah=',format(c,'09b'))

print('========OR========')
# tugas

print('========XOR========')
# tugas

print('\n========NOT========')
c = ~a
print('Nilai',a,'biner adalah     =',format(a,'09b'))
print('Nilai not',a,'biner adalah =',format(c,'09b'))

c = ~b
print('Nilai',b,'biner adalah     =',format(a,'09b'))
print('Nilai not',b,'biner adalah =',format(c,'09b'))

print('\n========Left Shift========')
c = a << 2
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',a,'<< 2 biner adalah =',format(c,'09b'))
c = b << 2
print('Nilai',b,'biner adalah      =',format(a,'09b'))
print('Nilai',b,'<< 2 biner adalah =',format(c,'09b'))

print('\n========Right Shift========')
c = a >> 2
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',a,'>> 2 biner adalah =',format(c,'09b'))
c = b >> 2
print('Nilai',b,'biner adalah      =',format(a,'09b'))
print('Nilai',b,'>> 2 biner adalah =',format(c,'09b'))


################

print()

print('===========NOT AND===========')
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',b,'biner adalah      =',format(b,'09b'))
print('----------------------------------------NOT AND')
c = ~(a & b)
print('Nilai',a,'not and',b,'biner adalah= ',format(c,'09b'))
#Tugas buat untuk NAND

print()
print('===========NOT OR===========')
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',b,'biner adalah      =',format(b,'09b'))
print('----------------------------------------NOT OR')
c = ~(a | b)
print('Nilai',a,'not or',b,'biner adalah= ',format(c,'09b'))
#Tugas buat untuk NOR

print()
print('===========NOT XOR===========')
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',b,'biner adalah      =',format(b,'09b'))
print('----------------------------------------NOT XOR')
c = ~(a ^ b)
print('Nilai',a,'not xor',b,'biner adalah= ',format(c,'09b'))
#Tugas buat untuk NXOR

print()
print('===========NOT << 2===========')
c = ~(a << 2)
print('Nilai',a,'biner adalah              =',format(a, '09b'))
print('Nilai',a,'not << 2 biner adalah     =',format(c, '09b'))

c = ~(b << 2)
print('Nilai',b,'biner adalah              =',format(b, '09b'))
print('Nilai',b,'not << 2 biner adalah     =',format(c, '09b'))
#Tugas buat untuk c = ~(a << 2)
#Tugas buat untuk c = ~(b << 2)

print()
print('===========NOT >> 2===========')
c = ~(a >> 2)
print('Nilai',a,'biner adalah              =',format(a, '09b'))
print('Nilai',a,'not >> 2 biner adalah     =',format(c, '09b'))

c = ~(b >> 2)
print('Nilai',b,'biner adalah              =',format(b, '09b'))
print('Nilai',b,'not >> 2 biner adalah     =',format(c, '09b'))
#Tugas buat untuk c = ~(a >> 2)
#Tugas buat untuk c = ~(b >> 2)
