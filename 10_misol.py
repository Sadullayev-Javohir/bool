"""Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring. A va B sonlarning faqat bittasi toq son."""

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))

print(A % 2 == 1 or B % 2 == 1)