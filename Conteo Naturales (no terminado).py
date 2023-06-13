''' 
Realizar un algoritmo que permita pedir 50 numero naturales y determine e 
imprima cuantos son pares, impares, positivos y negativos.
'''
count = int(input("Ingres "))
pa, im, po, ne = 0, 0, 0, 0
for i in range(count,26):

    if i % 2 == 0:
        pa =+ 1
        
    elif i % 3 == 0:
        im =+ 1
        
    elif i >= 0:
        po =+ 1
        
    else:
        ne =+ 1
        

print("El numero de pares en el conteo es: ", pa)
print("El numero de impares en el conteo es: ", im)  
print("El numero de positivos en el conteo es: ", po)
print("El numero de negativos en el conteo es: ", ne)
    