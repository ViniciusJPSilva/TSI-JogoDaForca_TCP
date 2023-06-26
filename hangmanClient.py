import os
import connection
import socket

def read_ip_address():
    '''
    Lê pelo dispositivo de entrada padrão um IP no formato de string, 
    valida e retorna o mesmo.
    '''
    message = "\nForneça o IP ou Hostname do servidor " 
    message += "(para LocalHost, basta pressionar ENTER): "

    while True:
        ip_address = input(message)
        if ip_address == "": 
            return connection.LOOPBACK_IP_ADDRESS
        else: 
            return ip_address
# read_ip_address()

def read_port():
    '''
    Lê pelo dispositivo de entrada padrão uma porta, 
    valida e retorna a mesma.
    '''
    while(True):
        try:
            port =  input("\nForneça a porta (para 14000, basta pressionar ENTER): ")
            if port == "":
                return connection.STD_PORT
            else:
                port = int(port)

            if connection.validate_port(port):
                return port
            else:
                raise ValueError()
        except ValueError:
            print("\nPorta inválida! Tente novamente.", end="")
    
# read_port()


def clear_terminal():
    '''
    Limpa o terminal.
    '''
    os.system('cls||clear')
# clear_terminal()


def start_game():
    '''
    Solicita o endereço do servidor, tenta realizar a conexão 
    e permite que o usuário jogue a partida.
    '''
    clear_terminal()
    print("\nBem vindo ao jogo da forca!")
    clientSocket = None
    try:
        while True:
            try:
                clientSocket = connection.create_client_connection(
                    read_ip_address(),
                    read_port())
                break
            except socket.gaierror:
                clear_terminal()
                print("\nIP ou Hostname inválido! Tente novamente.")
            except Exception:
                clear_terminal()
                print("\n\nOcorreu um erro durante a conexão com o servidor!" +
                      " Verifique os dados e tente novamente.")
    
        if clientSocket != connection.CONNECTION_REFUSED :
            while True:
                clear_terminal()
                messageFrom = clientSocket.recv(
                        connection.STD_MAX_PACKAGE_SIZE).decode(connection.UTF_8)
                if(messageFrom == connection.END_CONNECTION_MESSAGE): 
                    break
                if(messageFrom == connection.ERROR_MESSAGE): 
                    raise BrokenPipeError

                print(messageFrom, end = "")
                
                messageTo = input() + " "
                clientSocket.send(messageTo.encode(connection.UTF_8))

        else:
            print("Conexão recusada! Verifique se o servidor está ativado.")
    except BrokenPipeError:
        clear_terminal()
        print("Houve um erro com a conexão com o servidor! A aplicação será encerrada.")
    except KeyboardInterrupt:
        clear_terminal()
        print("A conexão foi interrompida!") 
    except Exception:
        clear_terminal()
    finally:
        print("Encerrando a conexão...")
        clientSocket.close
# start_game()


## main()
if __name__ == "__main__":
    start_game()