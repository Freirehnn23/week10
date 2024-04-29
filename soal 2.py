def menemukan_max_min(data):

  if len(data) < 2:
    raise ValueError("Harus memasukkan setidaknya dua nilai.")

  nilai_max = max(data[0], data[1])
  nilai_min = min(data[0], data[1])

  for value in data[2:]:
    nilai_max = value if value > nilai_max else nilai_max
    nilai_min = value if value < nilai_min else nilai_min

  return nilai_max, nilai_min

input_user = []
while True:
  nilai_input = input("Ketik angka yang ingin dimasukan, jika sudah ketik done): ")
  if nilai_input.lower() == "done":
    break
  input_user.append(float(nilai_input))


try:
  nilai_max, nilai_min = menemukan_max_min(input_user)
  print(f"Nilai Maksimumnya Adalah: {nilai_max}")
  print(f"Nilai Minimumnya Adalah: {nilai_min}")
except ValueError as e:
  print(f"Error: {e}")