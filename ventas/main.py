
clients = 'Irvyn, Erica, David'

def create_client(client_name):
    global clients # para evitar errores hacemos la varible de tipo global, con "global" para usarla dentro de la funcion
    
    if client_name not in clients: #not in operador para checar si está  dentro de la  lista de clientes
        clients += client_name
        _add_comma()
    else:
        print('Client already is in clien\'s list')


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients+= ', '


def _print_welcom():
    print('Bienvenidos a ventas')
    print('/*' * 50)
    print('What would you like to do today?')
    print('Create client')
    print('Delete client')


if __name__ == '__main__': # Aqui comienza nuestro codigo
    _print_welcom()
    command = input()#metodo para ingresar datos desde consola
    if command ==  'C': #Corre sin errores en python 3, versiones anteriores no
        client_name = input("What is the client name? ")
        create_client(client_name)
        list_clients()
    elif command == 'D':
        #Placeholder
        pass #pasar sin hacer  cosa alguna
    else:
        print('Invalid commmand')

    

