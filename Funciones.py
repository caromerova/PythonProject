

##estudiar sobre los principios SOLID, KISS, DRY

## Estructura de una funcion en python

## se define una funcion asi:   def my-function

##llamado de dicha funcion:  return "hola mundo"
## el llamado con el return es para que yo pueda reutilizar esas propiedades mas adelante, debo tener en cuenta que el llamado con el return No me pinta nada.
## las funciones tienen un punto de entrada
## repasar parametro vs argumento

##ejemplo completo de una funcion con return y prin, para poder manipular y pintar

## ejercicio de primer momento es entregar un ejercicio como este a continuacion. Completamente diferente, y es en la clase 5


employee_list = []
def register_employee():
    id = input("Id")
    employee_list.append(id)
    emp_name = input("Name")
    employee_list.append(emp_name)
    emp_lastname = input("Lastname")
    employee_list.append(emp_lastname)
    email = input("Email")
    employee_list.append(email)
    password = input("Password")
    employee_list.append(password)
    salary = int(input("Ingrese su salario"))
    employee_list.append(salary)
    
register_employee()
    
    
def print_employee_data():
    for emp in  employee_list:
        print(emp)
    
print(employee_list)


minimum_salary = 1300000

trans_aid = 1060000

def calculate_health_discount(salary):
    health_discount = salary * 0.04
    return health_discount


def calculate_morgate_discount(salary):
    morgate_discount = salary * 0.04
    return morgate_discount

def calculate_net_salary(salary, minimum_salary, trans_aid):
    health_discount = calculate_health_discount(salary)
    morgate_discount = calculate_morgate_discount(salary)
    if salary > 2*minimum_salary:
        net_salary = salary - health_discount - morgate_discount
    else:
        net_salary = salary - health_discount - morgate_discount + trans_aid
    
    return net_salary



def init_user_menu(init_session):
    if init_session == True:
        print("1.Data Employee\n 2. Employee Net Salary")   
        opc = int(input("Seleccione una opc"))
        match opc:
            case 1:
                print("Employee Data")
            case 2:
                print("Employee\n net salary")
                salary = employee_list[5]
                print(calculate_net_salary(salary, minimum_salary, trans_aid))
            case _:
                print("Seleccione una opcion valida")
            

##Ahora vamos a definir lo de iniciar sesion

def init_session():
    email = input("Email")
    password = input("password")
    if email == employee_list[3] and password == employee_list[4]:
        return True
    else: 
        return False
    
#init_session = init_session()
init_user_menu(init_session())

def menu_app():
    
    opc = int(input("1.Registrarse\n 2. Iniciar Sesion\n 3. Salir"))
    
    match opc:
        case 1:
            print("1. Regiistro")
            register_employee
        case 2:
            print("2. Iniciar Sesion")
            init_user_menu(init_session())                      
        case 3:
            print("3. Salir")
            init = 0
        case _:
            print("Ingrese una opcion valida")
        


def app():
    init = input("presione 1 para inicializar")
    while init != 0:
        menu_app()
        
app()
                     
