# -*- coding. utf-8 -*-
a, b = 0, 1
while a < 10:
    print(a)
    a,b = b, a+b
if a == 10:
    print("Fin")