nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
alamat = input("Masukkan alamat Anda: ")
kelas = input("Masukkan kelas Anda: ")
jurusan = input("Masukkan jurusan Anda: ")


biodata = """
Nama   : {}
Umur   : {} tahun
Alamat : {}
kelas   : {}
jurusan : {}
""".format(nama, umur, alamat, kelas, jurusan)

print(biodata)
