import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Hanya boleh memasukkan bilangan bulat.")
    sys.exit(1)

try:
    hasil = x / y
except ZeroDivisionError:
    print("Error: Tidak bisa dibagi dengan 0.")
    sys.exit(1)

print(f"{x} / {y} = {hasil}")