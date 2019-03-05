
clients = 'Irvyn, Erica, David'

def create_client(client_name):
    global clients # para evitar errores hacemos la varible de tipo global, con "global" para usarla dentro de la funcion
    _add_comma()
    clients += client_name
    _add_comma()


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients+= ', '


if __name__ == '__main__': # Aqui comienza nuestro codigo
    list_clients()
    create_client('Mari')
    list_clients()
    

