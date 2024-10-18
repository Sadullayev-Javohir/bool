"""Uch xonali son berilgan. Jumlani rostlikka tekshiring. Ushbu sonning raqamlari ketma-ket o'suvchi bo'lib 
joylashgan yoki kamayuvchi ketma-ketlikga ega."""

num = int(input("Son kiriting: "))

first = num // 100
second = (num // 10) % 10
third = num % 10

check = first < second < third or third < second < first

print(check)