import socket
import time
import ipaddress

STD_CLIENT_IP = ""
LOOPBACK_IP_ADDRESS = "127.0.0.1"

STD_PORT = 14000
STD_MAX_PACKAGE_SIZE = 2048
CONNECTION_ATTEMPTS = 5

UTF_8 = "utf-8"

END_CONNECTION_MESSAGE = "__END__"  # Flag que indica o término da conexão TCP.
CONNECTION_REFUSED = "__REFUSED__"


def create_server_connection(client=STD_CLIENT_IP, port=STD_PORT): 
    '''
    Cria um soquete servidor utilizando o protocolo TCP.
    client - ip do cliente, o padrão é STD_CLIENT_IP.
    port - número da porta, o padrão é  STD_PORT.

    retorna o soquete criado.
    '''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((client, port))
    server_socket.listen(0)

    return server_socket
# create_server_connection()


def create_client_connection(server, port=STD_PORT): 
    '''
    Cria um soquete cliente utilizando o protocolo TCP.
    servidor - ip do servidor.
    port - número da porta, o padrão é  STD_PORT.

    retorna o soquete criado.
    '''
    for attempt in range(1, CONNECTION_ATTEMPTS + 1):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server, port))

            return client_socket
        except ConnectionRefusedError:
            print("Tentando se conectar ao servidor... " +
                  f"Tentativa {attempt} de {CONNECTION_ATTEMPTS}")
            time.sleep(5)
    
    return CONNECTION_REFUSED
# create_server_connection()


def validate_ip_address(ip_address: str): #
    '''
    Valida se a string fornecida é um IP (IPv4 ou IPv6) válido.
    ip_address - ip que será validado.

    retorna True caso seja válido ou False caso não.
    '''
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False
# validate_ip_address()

def validate_port(port: int): #
    '''
    Valida se o número fornecido é uma porta válida.
    port - porta que será validada.

    retorna True caso seja válida ou False caso não.
    '''
    if port < 0 or port > 65535:
       return False
    else:
       return True
# validate_port()