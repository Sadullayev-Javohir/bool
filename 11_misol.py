"""Ikkita A va B butun sonlari berilgan. Jumlani rostlikka tekshiring. A va B sonlarining har ikkalasi ham
yoki toq son yoki juft son"""

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))

print((A % 2 == 1 and B % 2 == 1) or (A % 2 == 0 and B % 2 == 0))
