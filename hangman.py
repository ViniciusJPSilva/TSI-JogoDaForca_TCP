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
'abruptamente',
'absurdo',
'abismo',
'afixo',
'perguntar',
'avenida',
'estranho',
'axioma',
'azul',
'banda',
'banjo',
'baio',
'apicultor',
'bikini',
'blitz',
'nevasca',
'boggle',
'buckaroo',
'bufalo',
'palhaço',
'rechonchuda',
'urubu',
'zumbido',
'califa',
'arrogancia',
'croquete',
'cripta',
'coraçao',
'ciclo',
'recusar',
'vertiginosa',
'duplex',
'anoes',
'desviar',
'equipar',
'espionagem',
'exodo',
'fingindo',
'anzol',
'fixavel',
'falando',
'fofo',
'esgotado',
'frisado',
'engraçado',
'galaxia',
'galvanizar',
'mirante',
'aparelho',
'pirilampo',
'glifo',
'fofoca',
'grogue',
'acaso',
'hifen',
'geladeira',
'ferida',
'marfim',
'caminhada na rua',
'geleia',
'azar',
'joquei',
'corrida',
'brincadeira',
'jovial',
'alegre',
'suculento',
'jumbo',
'caiaque',
'caqui',
'quilobyte',
'quiosque',
'desajeitado',
'mochila',
'laringe',
'comprimentos',
'sortudo',
'luxo',
'linfa',
'marques',
'matriz',
'megahertz',
'microondas',
'mnemonico',
'mistificar',
'naftalina',
'boate',
'estupido',
'ninfa',
'ovario',
'oxidar',
'oxigenio',
'pijama',
'catarro',
'pixel',
'pneumonia',
'intrigante',
'quartzo',
'fila',
'brincadeiras',
'quixotesco',
'questionario',
'ritmo',
'schnapps',
'arranhar',
'estiloso',
'esfinge',
'espirrar',
'gritar',
'força',
'forças',
'esticar',
'fortaleza',
'bloqueado',
'transgredir',
'transplante',
'tritongo',
'desconhecido',
'indigno',
'descompactar',
'vaporizar',
'garota',
'vodka',
'vodu',
'passeio',
'valsa',
'aceno',
'ondulado',
'ceroso',
'fonte',
'chiado',
'zumbindo',
'covarde',
'feitiçaria',
'mago',
'tonto',
'xilofone',
'iate',
'jugo',
'jovem',
'delicioso',
'ziguezague',
'ziguezagueando',
'zero',
'zumbi',
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
        self.word = get_random_word(WORD_LIST)
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
        game_status += f"\nTentativas restantes: {self.player_live}"

        if self.last_status == STATUS_REPEATED_LETTER:
            game_status += f"\nA letra \'{self.letter}\' já foi utilizada!"
            game_status += " Tente novamente.\n"

        return game_status
    #

    ## Executa uma rodada.
    def run_the_round(self): #
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

	##
    def get_final_message(self): #
        message_to_cliente = self.get_game_status()

        if self.player_live > 0:
            message_to_cliente += "\n\nParabéns! VOCÊ VENCEU!\n\n"
        else:
            message_to_cliente += "\n\nVOCÊ PERDEU!\nA palavra misteriosa era:"
            message_to_cliente += f" \"{self.word}\".\n\n"

        return message_to_cliente + "Pressione 'ENTER' para finalizar\n"
    #
# class Game


## Escolhe uma palavra da lista, pseudo-aleatoriamente.
def get_random_word(word_list):  #
    return random.choice(word_list)
#


## Verifica se um caractere está presente em determinada string.
def check_letter_in_word(letter, word):  #
    return sum([1 for lt in word if letter == lt])
#


## Cria uma string que representa a palavra à ser adivinhada, 
# as letras ainda não reveladas são substituidas pelo caractere '_'.
def get_mistery_word(word, letters_revealed):  #
    m_word = ""
    for letter in word:
        m_word += (letter + "  ") if (letter in letters_revealed) else ("_  ")

    return m_word
#


## Revela um caracter aleatório da palavra à ser adivinhada.
def reveal_a_letter(word, letters_revealed, letters_used): #
    letters_list = list(word)
    while True:
        letter = random.choice(letters_list)
        if letter not in letters_revealed:
            letters_revealed.append(letter)
            letters_used.append(letter)
            return letter
#