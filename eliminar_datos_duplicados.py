mi_lista = [3,3,5,1,4,5,1,1,4,5,7,8,3]

mi_lista_auxiliar = []

for elemento in mi_lista:
    if elemento not in mi_lista_auxiliar:
        mi_lista_auxiliar.append(elemento)

print('La lista inicial es: ', mi_lista)
print('La lista sin duplicados es: ', mi_lista_auxiliar)        