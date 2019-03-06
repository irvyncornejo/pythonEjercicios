
clients = 'Irvyn, Erica, David'

def create_client(client_name):
    global clients # para evitar errores hacemos la varible de tipo global, con "global" para usarla dentro de la funcion
    
    if client_name not in clients: #not in operador para checar si está  dentro de la  lista de clientes
        _add_comma()
        clients += client_name
        _add_comma()
    else:
        print('Client already is in clien\'s list')


def list_clients():
    global clients

    print(clients)


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
        
    else:
        _not_client()

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',' , '')
    else:
         _not_client()


def _add_comma():
    global clients

    clients+= ', '


def _print_welcom():
    print('Bienvenidos a ventas')
    print('/*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')

def _get_client_name():# se pide el nombre del cliente 
    return input ('What is the client name? ')

def _not_client():
    return print('Client is not in client list')

if __name__ == '__main__': # Aqui comienza nuestro codigo
    _print_welcom()

    command = input()#metodo para ingresar datos desde consola
    command = command.upper()

    if command ==  'C': #Corre sin errores en python 3, versiones anteriores no
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name() 
        delete_client(client_name) #  Borramos el nombre del cliente 
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client_name = update_client_name.capitalize()
        update_client(client_name,update_client_name)
        list_clients()

    else:
        print('Invalid commmand')

    

