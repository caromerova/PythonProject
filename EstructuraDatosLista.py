



user_name = "pepito"

users = ["pepito", "Maria", "Juan", "Laura", "Pedro"]

print(type(users))

print(len(users)) ##para conocer el tamaño de la lista

print(users[0]) ##para conocer la posicion cero

users[2] = "Cesar"

print(users[2]) ## para cambiar algun elemento de posicion

## esto es slicing
print(users[1:3])

print(users[0:])


for user in users:
    print(user)

for i in range(5):
    print(users[i])

