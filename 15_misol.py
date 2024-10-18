"""Uchta A, B, C butun sonlari berilgan. Jumlani rostlikka tekshiring. A, B, C sonlardan faqat ikkitasi musbat
son."""

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
C = int(input("C sonni kiriting: "))

print((A > 0 and B > 0 and C < 0) or (A < 0 and B > 0 and C > 0) or (A > 0 and B < 0 and C > 0))