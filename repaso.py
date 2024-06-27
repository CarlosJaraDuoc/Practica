import csv
import time
import time

nums = [[]]

def suma():
    while True:
        try:
            op = int(input("Ingrese un número: "))
            nums.append(op)
            respuesta = int(input("¿Desea agregar otro número?\n1. Sí\n2. No\n"))
            if respuesta == 2:
                break
            else:
                continue
        except ValueError:
            print("Vuelva a intentarlo")
            continue
    return nums
suma()
print(nums)
