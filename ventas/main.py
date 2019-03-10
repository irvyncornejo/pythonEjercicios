import sys

# clients = 'Erica, Irvyn, David' cambiamos el tipo de dato que almacena los nombres de los clientes

clients = ['Erica', 'Irvyn']

def create_client(client_name):
    global clients # para evitar errores hacemos la varible de tipo global, con "global" para usarla dentro de la funcion
    
    if client_name not in clients: #not in operador para checar si está  dentro de la  lista de clientes
        clients.append(client_name)
        
    else:
        print('Client already is in clien\'s list')


def list_clients():# mostrar lista de clientes
    global clients
    for idx, client in enumerate (clients): # Está linea nos ayuda a daber el indece de los clientes 
        print(f'{idx}: {client}')# Mostrara el nombre y el id. correspondiente 


def update_client(client_name, update_client_name):#actualizacion de clientes
    global clients

    if client_name in clients:
        index = clients.index(client_name) # obtenemos el valor del index, para despues reasignarlo
        clients[index] = updated_name
        
    else:
        _not_client()

def search_client(client_name): #busqueda de clientes
    global clients

    for client in clients: # Busca el cliente en la lista de clientes
        if client != client_name: # si el cliente buscado es diferente al nombre del cliente dentro de  la lista 
            continue # haz lo que sigue
        else:
            return True



def delete_client(client_name): #Borrar cliente
    global clients

    if client_name in clients:
        clients.remove(client_name) # Removemos el nombre del cliente en la lista por medio del valor del nombre
    else:
         _not_client()


def _print_welcom():
    print('Bienvenidos a ventas')
    print('/*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print ('[S]earch client')

def _get_client_name():# se pide el nombre del cliente 
    client_name = None # Uso de None para definir que la variables no contiene datos en ese momento
    while not client_name:
        client_name = input('What is the client name? ')
    
        if client_name == 'exit': # si el valor ingresado es exit
            client_name = None # se reasigna el valor de la variable y se deja vacia para pasar por una caja vacia y salir de la ejecucion
            break # se rompe y pasa al if not client_name: y se sale de la plicación

    if not client_name:
        sys.exit() # salir de  la ejecución del  programa

    return client_name

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

    elif command == 'R':
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
    
    elif command == 'S':
        client_name = _get_client_name()
        client_name = client_name.capitalize()
        found = search_client(client_name)
        if found: # Retorna es False o True
            #placeholder {} para conquetar el valor de una variable
            print ('The client: {} is in the client\' list'.format(client_name))# se concatena la variable nombre del cliente  
        else:
            print('The client: {} is not in our client\' list'.format(client_name))
    
    else:
        print('Invalid commmand')

    

