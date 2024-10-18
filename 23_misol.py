"""Uch xonali son berilgan. Jumlani rostlikka tekshiring. Ushbu sonni chapdan o'qiganda ham, o'ngdan o'qiganda
ham bir xil."""

num = int(input("Son kiriting: "))

first = num // 100
third = num % 10

check = first == third

print(check)