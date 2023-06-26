import hangman as hman
import connection
import threading

def check_play_again(answer: str): #
    answer = answer.lower()
    if (answer[0] == 's' or answer.strip() == ""):
        return True
    return False
#

def new_client(connection_socket, address):
    '''
    Função responsável por criar e gerenciar um novo jogo para o cliente informado.
    connection_socket: soquete do cliente
    address: endereço IP do cliente
    '''
    
    try:
        while True:
            game = hman.Game()
            # Loop de execução do jogo.
            while (not game.over()): #
                # Obtendo o status do jogo.
                message_to_client = game.get_game_status() + "\nTente acertar uma letra"
                message_to_client += (" (revelar letra = 0)" if (
                    not game.used_tip) else "")
                message_to_client += ": "
                connection_socket.send(message_to_client.encode(connection.UTF_8))

                # Recebendo a resposta
                message_client_response = connection_socket.recv(
                    connection.STD_MAX_PACKAGE_SIZE).decode(connection.UTF_8).lower()
                game.letter = str(message_client_response[0] 
                                if (len(message_client_response) > 0) else 1)

                # Executando a rodada.
                game.run_the_round()
                
            # while()

            # Finalização do jogo.
            message_to_cliente = game.get_final_message()
            connection_socket.send(message_to_cliente.encode(connection.UTF_8))

            # Verifica se o cliente gostaria de jogar novamente.
            if not check_play_again(connection_socket.recv(
                connection.STD_MAX_PACKAGE_SIZE).decode(connection.UTF_8).lower()):
                break

        # while()
        connection_socket.send(connection.END_CONNECTION_MESSAGE.encode(connection.UTF_8))
        print(f"\nO cliente {address} finalizou o jogo!")  
    except BrokenPipeError:
        print(f"\nHouve um erro com a conexão com o cliente {address}!")
    except KeyboardInterrupt:
        pass
    except Exception:
        pass
    finally:
        connection_socket.close()
# new_client()


def start_game():
    '''
    Cria um soquete servidor, inicia as conexões TCP 
    e gerencia as Threads dos clientes conectados.
    '''
    connected_clients_threads = []
    try:
        server_socket = connection.create_server_connection()
        while True:
            # Iniciando a conexão TCP
            print("\nAguardando novas conexões... Pressione CTRL + C para finalizar.")
            connection_socket, address = server_socket.accept()

            # Mensagem
            print(f"\nUm novo jogo foi iniciado por {address[0]}!")
            thread = threading.Thread(target=new_client, 
                                      args=(connection_socket, address[0]))
            connected_clients_threads.append((thread, connection_socket))
            thread.setDaemon(True)
            thread.start()
    except KeyboardInterrupt:
        print("\nA aplicação foi finalizada!") 
    finally:
        # Força o encerramento de todas as Threads filhas.
        for thread, connection_client in connected_clients_threads:
            try:
                connection_socket.send(connection.ERROR_MESSAGE.encode(connection.UTF_8))
            except OSError: # Caso tenha ocorrido falha na conexão de algum cliente.
                pass
            connection_client.close()
            thread.join(0)
        server_socket.close()
        
# start_game()


## main()
if __name__ == "__main__":
    start_game()