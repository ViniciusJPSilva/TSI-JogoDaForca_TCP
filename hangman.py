import random

'''
Módulo responsável por definir constantes, classes e 
funções para o jogo da forca (hangman).
'''

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

WORD_LIST = [
    ("banana", "Fruta"),
    ("computador", "Eletrônico"),
    ("girafa", "Animal"),
    ("praia", "Lugar"),
    ("avião", "Transporte"),
    ("chocolate", "Doce"),
    ("guitarra", "Instrumento"),
    ("piano", "Instrumento"),
    ("futebol", "Esporte"),
    ("livro", "Objeto"),
    ("arco", "Objeto"),
    ("coelho", "Animal"),
    ("caneta", "Escrita"),
    ("abacaxi", "Fruta"),
    ("janela", "Construção"),
    ("peixe", "Animal"),
    ("teclado", "Periférico"),
    ("pizza", "Comida"),
    ("tigre", "Animal"),
    ("espada", "Arma"),
    ("carro", "Veículo"),
    ("ventilador", "Eletrodoméstico"),
    ("melancia", "Fruta"),
    ("flor", "Planta"),
    ("cachorro", "Animal"),
    ("sol", "Astro"),
    ("cadeira", "Móvel"),
    ("avião", "Transporte"),
    ("telefone", "Comunicação"),
    ("chapéu", "Acessório"),
    ("sorvete", "Gelado"),
    ("leão", "Animal"),
    ("violão", "Instrumento"),
    ("sapato", "Calçado"),
    ("elefante", "Animal"),
    ("tesoura", "Corte"),
    ("computador", "Eletrônico"),
    ("abelha", "Inseto"),
    ("cenoura", "Vegetal"),
    ("relógio", "Tempo"),
    ("bola", "Objeto"),
    ("lápis", "Escrita"),
    ("cadeado", "Segurança"),
    ("borboleta", "Inseto"),
    ("música", "Som"),
    ("água", "Líquido"),
    ("mel", "Doce"),
    ("galinha", "Animal"),
    ("papagaio", "Animal"),
    ("óculos", "Acessório"),
    ("morango", "Fruta"),
    ("meia", "Vestuário"),
    ("escola", "Instituição"),
    ("planta", "Vegetal"),
    ("tesouro", "Valioso"),
    ("ônibus", "Transporte"),
    ("rosa", "Flor"),
    ("café", "Bebida"),
    ("sol", "Astro"),
    ("dinossauro", "Animal"),
    ("camisa", "Vestuário"),
    ("cama", "Móvel"),
    ("copo", "Utensílio"),
    ("pipoca", "Lanche"),
    ("peru", "Animal"),
    ("telefone", "Comunicação"),
    ("chave", "Acesso"),
    ("gato", "Animal"),
    ("computador", "Eletrônico"),
    ("elefante", "Animal"),
    ("leão", "Animal"),
    ("jardim", "Ambiente"),
    ("banana", "Fruta"),
    ("caixa", "Recipiente"),
    ("cachorro", "Animal"),
    ("viagem", "Deslocamento"),
    ("mala", "Bagagem"),
    ("macaco", "Animal"),
    ("pasta", "Escritório"),
    ("abacate", "Fruta"),
    ("trator", "Veículo"),
    ("fogo", "Elemento"),
    ("banana", "Alimento"),
    ("cachecol", "Acessório"),
    ("lâmpada", "Iluminação"),
    ("abajur", "Iluminação"),
    ("zebra", "Animal"),
    ("mar", "Corpo de água"),
    ("avião", "Viagem"),
    ("eletricidade", "Energia"),
    ("capacete", "Proteção"),
    ("helicoptero", "Transporte"),
    ("coqueiro", "Árvore"),
    ("sorvete", "Gelado"),
    ("tubarão", "Animal"),
    ("fada", "Personagem"),
    ("sapato", "Calçado"),
    ("morango", "Fruta"),
    ("escada", "Acesso"),
    ("navio", "Embarcação"),
    ("computador", "Tecnologia"),
    ("batata", "Vegetal"),
    ("travesseiro", "Conforto"),
    ("melancia", "Fruta"),
    ("abelha", "Inseto"),
    ("cachorro", "Animal"),
    ("vela", "Iluminação"),
    ("microfone", "Áudio"),
    ("espelho", "Reflexo"),
    ("celular", "Dispositivo"),
    ("oculos", "Acessório"),
    ("piano", "Instrumento"),
    ("bicicleta", "Veículo"),
    ("fechadura", "Segurança"),
    ("espelho", "Reflexo"),
    ("neve", "Clima"),
    ("escova", "Higiene"),
    ("panda", "Animal"),
    ("bússola", "Orientação"),
    ("berço", "Móvel"),
    ("fantasma", "Assombração"),
    ("lanterna", "Iluminação"),
    ("aranha", "Inseto"),
    ("navalha", "Corte"),
    ("lousa", "Educação"),
    ("carro", "Automóvel"),
    ("chocolate", "Doce"),
    ("raio", "Descarga"),
    ("escultura", "Arte"),
    ("camiseta", "Vestuário"),
    ("sorvete", "Gelado"),
    ("ventilador", "Eletrodoméstico"),
    ("criptografia", "Segurança"),
    ("exorbitante", "Exagero"),
    ("inextricável", "Complicado"),
    ("paradigma", "Conceito"),
    ("perspicaz", "Inteligente"),
    ("ubíquo", "Omnipresente"),
    ("efêmero", "Passageiro"),
    ("idiossincrasia", "Característica"),
    ("magnânimo", "Generoso"),
    ("nefarious", "Perverso"),
    ("plenipotenciário", "Autoridade"),
    ("efervescente", "Borbulhante"),
    ("inebriante", "Embebedante"),
    ("quimera", "Ilusão"),
    ("taciturno", "Silencioso"),
    ("vociferante", "Barulhento"),
    ("disseminar", "Espalhar"),
    ("iconoclasta", "Destruidor de ídolos"),
    ("obsequioso", "Servil"),
    ("inexorável", "Inflexível"),
    ("quixotesco", "Idealista"),
    ("efímero", "Breve"),
    ("intransigente", "Rígido"),
    ("procrastinar", "Adiar"),
    ("zenith", "Culminação"),
    ("arcano", "Misterioso"),
    ("ebulição", "Ebulição"),
    ("inefável", "Indescritível"),
    ("paroxismo", "Auge"),
    ("inócuo", "Inofensivo"),
    ("reles", "Insignificante"),
    ("alhures", "Em outro lugar"),
    ("convalescença", "Recuperação"),
    ("paradisíaco", "Paradisíaco"),
    ("sagaz", "Astuto"),
    ("ambivalente", "Contraditório"),
    ("endiabrado", "Perverso"),
    ("meticuloso", "Cuidadoso"),
    ("pretensioso", "Presunçoso"),
    ("atemporal", "Eterno"),
    ("equanimidade", "Calma"),
    ("neófito", "Novato"),
    ("suplício", "Tortura"),
    ("vacilante", "Indeciso"),
    ("demagogo", "Manipulador"),
    ("exorbitante", "Excessivo"),
    ("inexorável", "Impiedoso"),
    ("quimérico", "Fantástico"),
    ("sublime", "Excepcional"),
    ("zen", "Meditação"),
    ("subterfúgio", "Evasão"),
    ("hipotético", "Suposto"),
    ("insólito", "Estranho")
]

LOGO = (
    "      _                             _           ______\n"
    "     | |                           | |         |  ____|\n"
    "     | |  ___    __ _   ___      __| |  __ _   | |__     "
    "___   _ __   ___   __ _\n"
    " _   | | / _ \\  / _` | / _ \\    / _` | / _` |  |  __|   "
    "/ _ \\ | '__| / __| / _` |\n"
    "| |__| || (_) || (_| || (_) |  | (_| || (_| |  | |     "
    "| (_) || |   | (__ | (_| |\n"
    " \\____/  \\___/  \\__, | \\___/    \\__,_| \\__,_|  |_|    "
    "  \\___/ |_|    \\___| \\__,_|\n"
    "                 __/ |\n"
    "                |___/\n"
)

LOGO_EN = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Constantes de controle
STATUS_MISS = 0
STATUS_HIT = 1
STATUS_REPEATED_LETTER = -1

TIP_FLAG = '0'

# Vidas máximas
MAX_LIVES = len(HANGMANPICS) - 1


class Game: #
    '''
    Classe base para o jogo da forca, define todos os status do jogo, 
    como número de vidas, palavra misteriosa e acertos.
    '''
    def __init__(self): #
        self.player_live = MAX_LIVES
        self.word, self.tip = get_random_word(WORD_LIST)
        self.word_length = len(self.word)
        self.hits = 0
        self.letters_revealed = []
        self.letters_used = []
        self.last_status = STATUS_HIT
        self.letter = ''
        self.used_tip = False
    #

	
    def over(self): #
        '''
        Verifica se o jogo terminou. Retorna True caso sim ou False caso não.
        '''
        return not (self.player_live > 0 and self.hits < self.word_length)
	#

    
    def get_game_status(self):  #
        '''
        Gera uma string com diversos status do jogo.
        '''
        game_status = f"{LOGO}\n\nPalavra misteriosa:\n\n"
        game_status += get_mistery_word(self.word, self.letters_revealed)
        game_status += f"\n\n{HANGMANPICS[MAX_LIVES - self.player_live]}"
        game_status += f"\nDica: {self.tip}"
        game_status += f"\nTentativas restantes: {self.player_live}"

        if self.last_status == STATUS_REPEATED_LETTER:
            game_status += f"\nA letra \'{self.letter}\' já foi utilizada!"
            game_status += " Tente novamente.\n"

        return game_status
    #

    
    def run_the_round(self): #
        '''
        Executa uma rodada.
        '''
        self.last_status = STATUS_HIT

        # Verifica se a tentativa é uma letra.
        if str(self.letter).isalpha():  
            # Verifica se já foi usada/adivinhada.
            if self.letter not in self.letters_used:    
                # Verifica se a letra da tentativa está presente na palavra misteriosa.
                check = check_letter_in_word(self.letter, self.word)  
                if check > 0:
                    self.hits += check
                    self.letters_revealed.append(self.letter)   # Revela a letra.
                else:
                    self.last_status = STATUS_MISS
                    self.player_live -= 1   # Decrementa as vidas restantes.
            
                self.letters_used.append(self.letter)
            else:
                self.last_status = STATUS_REPEATED_LETTER
        # Flag de dica: Verifica se a dica foi utilizada.
        elif self.letter == TIP_FLAG and not self.used_tip: 
            self.used_tip = True
            # Revela uma letra aleatória da palavra misteriosa.
            self.hits += check_letter_in_word(  
                        reveal_a_letter(self.word, self.letters_revealed, 
                                        self.letters_used),
                        self.word)
    #


    def get_final_message(self): #
        '''
        Retorna a mensagem de finalização do jogo.
        '''
        message_to_cliente = self.get_game_status()

        if self.player_live > 0:
            message_to_cliente += "\n\nParabéns! VOCÊ VENCEU!\n\n"
        else:
            message_to_cliente += "\n\nVOCÊ PERDEU!\nA palavra misteriosa era:"
            message_to_cliente += f" \"{self.word}\".\n\n"

        return message_to_cliente + "Pressione 'ENTER' para finalizar\n"
    #
# class Game


def get_random_word(word_list):  #
    '''
    Escolhe uma palavra da lista, pseudo-aleatoriamente.
    '''
    return random.choice(word_list)
#


def check_letter_in_word(letter, word):  #
    '''
    Verifica se um caractere está presente em determinada string.
    '''
    return sum([1 for lt in word if letter == lt])
#


def get_mistery_word(word, letters_revealed):  #
    '''
    Cria uma string que representa a palavra à ser adivinhada, 
    as letras ainda não reveladas são substituidas pelo caractere '_'.
    '''
    m_word = ""
    for letter in word:
        m_word += (letter + "  ") if (letter in letters_revealed) else ("_  ")

    return m_word
#


def reveal_a_letter(word, letters_revealed, letters_used): #
    '''
    Revela um caracter aleatório da palavra à ser adivinhada.
    '''
    letters_list = list(word)
    while True:
        letter = random.choice(letters_list)
        if letter not in letters_revealed:
            letters_revealed.append(letter)
            letters_used.append(letter)
            return letter
#