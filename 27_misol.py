"""x, y sonlar berilgan. Jumlani rostlikka tekshiring. Koordinatalari (x, y) bo'lgan nuqta koordinata choragining
ikkinchisida yoki uchinchisida yotadi."""

x = int(input("x koordinata kiriting: "))
y = int(input("y koordinata kiriting: "))

check = (x < 0 and y > 0) or (x < 0 and y < 0)

print(check)