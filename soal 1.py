def tiga_terbaik():
  while True:
      nilai1 = float(input("Masukkan nilai 1: "))
      nilai2 = float(input("Masukkan nilai 2: "))
      nilai3 = float(input("Masukkan nilai 3: "))
      nilai4 = float(input("Masukkan nilai 4: "))
      nilai5 = float(input("Masukkan nilai 5: "))

      if not all([isinstance(n, float) for n in [nilai1, nilai2, nilai3,nilai4,nilai5]]):
        raise ValueError("Semua nilai harus berupa angka.")

      data = [nilai1, nilai2, nilai3,nilai4,nilai5]
      data.sort(reverse=True)

      return data[:3]


hasil = tiga_terbaik()
print(f"Tiga nilai terbaik: {hasil}")