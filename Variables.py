

# Esto es un comentario
# Variables (son dinámicas) es decir no es necesario tipar los datos aunque permite hacerlo, pero Python antepone o forza el dinamismo.

# ejemplo:

name = "Maria"

lastName: str = "Castro"

number: int = "dos"

print(type(number))

# let´s g t create 

note = 4.35

print(type(note))

# other
age = 29

print(type(age))

# now a boolean

isActive = True
print(type(isActive))

# Now a example whit a list

ages = [15,19,21,30]
print(type(ages))

#other example of a list

weeks_days = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(type(weeks_days))

# other example

user = {"Name": "Maria", "Age": 19}
print(type(user))

# other example

notes = {4.5, 2.8, 3.6, 4.7}
print(type(notes))

# other example
num1 = int(input("Agregue el numero 1 y sumelo con el 2"))

sum = num1 + 2
print("El resultado es " , sum)
#print("El resultado es " , sum)
print(f"El resultado es {sum}")

# declaremos una funcion con ejemplo de error de indentacion (el error esta en los espacios)

#def sum(num1):
#num1 + 2
#return sum

# ahora definamos bien la funcion

def sum2(num1):
    num2 = 2
    return  num1 + num2

result = sum2(num1)
print(f"el resultado de la suma es {result}")