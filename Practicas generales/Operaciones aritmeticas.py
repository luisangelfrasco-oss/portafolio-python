number_1=42
number_2=34

sum_numbers= number_1 + number_2
print('integer addition:', sum_numbers)
print(sum_numbers)

#al hacer "variable total= variable 1 + variahble 2" se suman los valores de las variables y se asigna el resultado a la variable total, a la hora de imprimir la variable total se mostrara el resultado de la suma de las variables 1 y 2
#el integer addition es solo la forma de escribirn o indicar que es la suma y no afecta al resultado de la operacion

number_3= 12.5
number_4= 3.5
subtraction_numbers= number_3 - number_4
print('float subtraction:', subtraction_numbers)
print(subtraction_numbers)

division_numbers= number_1 / number_2
print('integer division:', division_numbers)
print(division_numbers)

multiplication_numbers= number_1 * number_2


print(isinstance(precio,(int,float)))
precio="e"
def descuento(precio, porcentaje):
    if isinstance(precio, (int, float)) and isinstance(porcentaje, (int, float))!=True:

        print("el numero debe ser un entero o un flotante")
