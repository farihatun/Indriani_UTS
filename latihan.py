# Program Penentuan Nilai Tempat Bilangan

# Meminta input dari pengguna
number = input("Masukkan bilangan: ")

# Mengubah bilangan menjadi list digit
digits = list(number)

# Menentukan panjang digit
length = len(digits)

# Daftar nama nilai tempat
places = ["satuan", "puluhan", "ratusan", "ribuan", "puluh ribuan",
          "ratus ribuan", "jutaan", "puluh jutaan", "ratus jutaan"]

# Output
print(f"Anda memasukkan bilangan {number} dimana:")

# Perulangan untuk menampilkan nilai tempat
for i in range(length):
    print(digits[i], "merupakan", places[length - i - 1])
