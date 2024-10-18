"""Uch xonali son berilgan. Jumlani rostlikka tekshiring. Ushbu sonning barcha raqamlari har xil."""

num = int(input("Son kiriting: "))

first = num // 100
second = (num // 10) % 10
third = num % 10

check = first != second and second != third and third != first

print(check)