nama = str (input('Nama karyawan: '))
pendapatan = float(input("Masukkan pendapatan karyawan: "))

if pendapatan >= 1000:
    status = 'Status: Berhak'
else:
    status = 'Status: Tidak Berhak'

print(status)
