
# ejemplo de casteo
num1 = int(input("agregue el primer numero"))

num2 = int(input("agregue el segundo numero"))

suma = num1 + num2
rest = num1 - num2
mult = num1 * num2
div= num2 / num1
mod = num2 % num1

print(f"el resultado de la suma es {sum}")
print(f"el resultado de la resta es {rest}")
print(f"el resultado de la multiplicacion  es {mult}")
print(f"el resultado de la division es {div}")
print(f"el resultado del modulo es {mod}")

# Operadores de comparacion

greatest_than = num1 > num2
less_than = num2 < num1
great_equal = num1 >= num2
less_equal = num2 <= num1
equal = num1 == num2
not_equal = num2 != num1

print(great_equal)
print(greatest_than)
print(less_than)
print(less_equal)
print(equal)
print(not_equal)

# Operadores Logicos

is_true = False and True

print(is_true)

is_false = False or True

# Operadores de Asignacion = , += , -= , *=, /=

num1 = num1 + num2

num2 += num1

# Gerarquia de operadores como recordatorio para seguir avanzando en este proyecto 
"""

    1. ()
    2. ^ , rad
    3. * , /, %
    4. +, -
    5. >, <, >= , <= , == , !=
    6. =, +=, -=, /=

"""
