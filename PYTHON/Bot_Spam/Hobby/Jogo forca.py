import random

FORCAIMG = ['''

   +---+
   |   |
       |
       |
       |
       |
==========''','''

   +---+
   |   |
   o   |
       |
       |
       |
==========''','''

   +---+
   |   |
   o   |
   |   |
       |
       |
==========''','''

   +---+
   |   |
   o   |
  /|   |
       |
       |
==========''','''

   +---+
   |   |
   o   |
  /|\  |
       |
       |
==========''','''

   +---+
   |   |
   o   |
  /|\  |
  /    |
       |
==========''','''

   +---+
   |   |
   o   |
  /|\  |
  / \  |
       |
==========''']

palavras = 'banana telescópio cachorro martelo girafa hambúrguer chocolate alimentos biscoito carne supermercado açougue tia tio pai mãe'.split()
def main():
    global FORCAIMG
    print('F O R C A')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True

    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        palpite = recebaPalpite(letrasErradas + letrasAcertadas)
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é " +palavraSecreta+'!Você ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG)-1:
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
                print("Você excedeu o seu limite de palpites!")
                print("Depois de "+str(len(letrasErradas))+' letras erradas e '+str(len(letrasAcertadas)), end = ' ')
                print("Palpites corretos, a palavra era "+palavraSecreta+'.')
                jogando = False

        if not jogando:
            if jogarNovamente():
                letrasErradas = ''
                letrasAcertadas = ''
                jogando = True
                palavraSecreta = geraPalavraAleatória().upper()


def geraPalavraAleatória():
    """
    Função que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)
    
def imprimeComEspaços(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa
    com espaço entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end = '')
    print()
        

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variável global que contém as imagens
    do jogo em ASCII art, e também as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)] + '\n')

    print("Letras Erradas: ", end = ' ')
    imprimeComEspaços(letrasErradas)

    vazio = '_'*len(palavraSecreta)

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]

    imprimeComEspaços(vazio)
    
def recebaPalpite(palpitesFeitos):
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado
    """
    while True:
        print()
        palpite = input("Advinhe uma letra. \n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra. \n")
        elif palpite in palpitesFeitos:
            print("Essa letra já existe, digite outra. \n")
        elif not 'A' <= palpite <= 'z':
            print("Insira apenas letras.")
        else:
            return palpite

        
def jogarNovamente():
    """
    Função que pede para o usuário pedir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """

    return input("Você quer jogar novamente? (Sim ou Não) \n").upper().startswith('S')
    
    
def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    """
    Função que verifica se o usuário acertou todas
    as letras da palavra secreta
    """
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou

main()

    
