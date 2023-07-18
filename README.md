# TSI-Jogo Da Forca
 
O objetivo deste trabalho é desenvolver um jogo da forca clássico, em terminal, utilizando soquetes e conexões TCP.

![image](https://github.com/ViniciusJPSilva/TSI-Jogo_Da_Forca_TCP/assets/81810017/e8c9ef6a-8dda-4bad-84e0-81299488cf8e)
<hr>

Existem 2 executáveis principais:

- O servidor: responsável por gerenciar os clientes e executar todo o processamento do jogo.
- Os clientes: responsáveis por se conectarem ao servidor, receberem os dados (status do jogo em formato de texto) e enviarem tentativas (letras) ou comandos de conexão.
  
<hr>

O servidor utiliza threads para "executar" individualmente o jogo de cada cliente conectado.

 ![image](https://github.com/ViniciusJPSilva/TSI-Jogo_Da_Forca_TCP/assets/81810017/ad593cab-de0f-41ab-98f1-69a5cd800808)

<hr>
