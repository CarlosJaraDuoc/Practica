dic_user = {'viccos':'1234',
            'viccas':'9876',
            'basroj':'6543'}
usuario = ''
usuario = input("Ingrese clave a buscar: ")
if dic_user.get(usuario,'no existe') == 'no existe':
    print("usuario no existe")
else:
    print("usuario existe")