"""Musbat butun son berilgan. Jumlani rostlikka tekshiring. Berilgan son uch xonali toq"""

num = int(input("Son kiriting: "))

check = num <= 999 and num >= 100 and num % 2 == 1

print(check)