# operadores de conversion
# upper - convierte a mayusculas
# lower - convierte a minusculas
# find - Encuentra el indice dentro de un patron que nosotros definimos
# startswith - El string comienza con algun patron
# endswith - El string termina con algun patron
# capitalize - Que la  primera letra sea mayuscula y lo demas en minusculas

# operadores de pertenencia 
# in - pertence
# not in - no pertence 

nombre = 'Cualitec'
# print(nombre.upper())
# # Encuentra el patron devuelve el indice en donde se encuentra
# print(nombre.find('ec'))
# # Devuelve un valor True si la palabra comienza con ese patron o letra
# print (nombre.startswith('C'))
# # Devuelve un valor True si la palabra termina con ese patron o letra
# print (nombre.endswith('z'))
# # Convierte el string de tal manera que la primera letra es mayuscula
# print(nombre.capitalize())

# funciones auxiliares para saber que podemos hacer con los elementos dir(nombre) y nos devueleve los  metodos 
#que podemos usara con dicho valor
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
def help_function():#Función de ayuda
    """ Este es untexto de ayuda de como utilizar esta función"""
    pass


def convertir_dato(dato, eleccion):
    if eleccion == 'M':
        print(dato.upper())

    elif eleccion == 'm':
        print(dato.lower())

    elif eleccion == 'n':
        print(dato.capitalize())

    else: 
        print('Opción no valida')


def _instrucciones_uso():
    print('Para convertir mayuculas ingresar, M ')
    print('Para convertir a minusculas ingresar, m ')
    print('Si es nombre propio, n ')


if __name__ == "__main__":
    help(help_function)
    _instrucciones_uso()
    dato = input('Ingresa la palabra: ')
    eleccion = input('Ingresa lo que deseas hacer  ')
    convertir_dato(dato, eleccion)
    dir(nombre)

