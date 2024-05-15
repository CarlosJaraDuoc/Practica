import os
import time
saldo = 120000
while True:
    while True:
        try:
            os.system("cls")
            print(f"Saldo actual: ${saldo}")
            print("Seleccione una opción:")
            print("1. Depositar dinero.")
            print("2. Retirar dinero.")
            opcion = int(input())
            if opcion == 2 and saldo <= 0:
                print("No hay saldo disponible para retirar")
                print(f"Usted tiene: ${saldo} actualmente")
            if opcion == 1:
                while opcion == 1:
                    try:
                        os.system("cls")
                        print(f"Usted tiene: ${saldo} de saldo en su cuenta.")
                        deposito = int(input("Ingrese monto para deposito: "))  
                        if deposito <= 0:   
                            print("Saldo insuficiente")
                            time.sleep(2)
                            continue
                        else:
                            saldo += deposito
                            print("Deposito exitoso")
                            print(f"Saldo restante: ${saldo}")
                            time.sleep(2)
                            opcion = 0
                            break
                    except ValueError:
                        print("Valor no válido")
                        time.sleep(2)
                        continue
            elif opcion == 2 and saldo > 0:
                while opcion == 2:
                    try:
                        os.system("cls")
                        print(f"Usted tiene: ${saldo} máximo para retirar.")
                        retiro = int(input("Ingrese monto para retiro: "))
                        if retiro <= saldo:
                            saldo -= retiro
                            print("Retiro exitoso")
                            print(f"Saldo restante: ${saldo}")
                            time.sleep(2)
                            opcion = 0
                            break
                        else:  
                            print("Saldo insuficiente")                         
                            time.sleep(2)
                            continue
                    except ValueError:
                        print("Valor no válido")
                        time.sleep(2)
                        continue
            else:
                print("Solo puede ingresar el número 1 o 2")
                time.sleep(2)
                continue
        except ValueError:
            print("Valor no válido")
            time.sleep(2)
            continue
        while True:
            try:
                print("¿Desea continuar con el cajero?: ")
                print("1. si")
                print("2. No")
                otro = int(input())
                if otro == 1:
                    time.sleep(2)
                    break
                elif otro == 2:
                    time.sleep(2)
                    break
                else:
                    print("Solo puede ingresar el número 1 o 2")
                    time.sleep(2)
                    continue
            except ValueError:
                print("Valor no válido")
                time.sleep(2)
                continue
        if otro == 1:
            time.sleep(1)
            break
        else:
            print("Gracias por usar el cajero")
            time.sleep(2)
            break
    if otro == 1:
            continue
    else:
        break