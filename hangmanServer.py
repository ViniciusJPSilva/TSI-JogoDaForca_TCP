import hangman as hman
import connection
import threading

def new_client(connection_socket, address):
    '''
    Função responsável por criar e gerenciar um novo jogo para o cliente informado.
    connection_socket: soquete do cliente
    address: endereço IP do cliente
    '''
    game = hman.Game()
    try:
        # Loop de execução do jogo.
        while (not game.over()): #
            # Obtendo o status do jogo.
            message_to_client = game.get_game_status() + "\nTente acertar uma letra" 
            message_to_client += (" (dica = 0)" if (not game.used_tip) else "") + ": "
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

        # Finaliza a conexão do cliente.
        connection_socket.recv(connection.STD_MAX_PACKAGE_SIZE)
        connection_socket.send(connection.END_CONNECTION_MESSAGE.encode(connection.UTF_8))
        print(f"\nO cliente {address} finalizou o jogo!")  
    except BrokenPipeError:
        print(f"\nHouve um erro com a conexão com o cliente {address}!")
    except KeyboardInterrupt:
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
            # Iniciando a conexão p2p TCP
            print("\nAguardando novas conexões... Pressione CTRL + C para finalizar.")
            connection_socket, address = server_socket.accept()

            # Mensagem
            print(f"\nUm novo jogo foi iniciado por {address[0]}!")
            thread = threading.Thread(target=new_client, 
                                      args=(connection_socket, address[0]))
            connected_clients_threads.append(thread)
            thread.setDaemon(True)
            thread.start()
    except KeyboardInterrupt:
        print("\nA aplicação foi finalizada!") 
    finally:
        # Força o encerramento de todas as Threads filhas.
        for thread in connected_clients_threads:
            thread.join(0)
        server_socket.close()
# start_game()


## main()
if __name__ == "__main__":
    start_game()