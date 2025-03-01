# Importa o módulo 'pygame' para desenvolver jogos e
        # interfaces gráficas em Python.
import pygame

# Importa o módulo 'sys' que provê acesso a algumas variáveis e 
        # funções que interagem com o interpretador Python.
import sys

# Importa o módulo 'random' que contém funções para geração 
        # de números aleatórios.
import random

# Importa o módulo 'os' que fornece uma forma portável de usar 
        # funcionalidades dependentes do sistema operacional.
import os

# A função 'pygame.init()' inicializa todos os módulos incluídos no 
        # pygame, preparando a biblioteca para seu uso.
pygame.init()

# Define as dimensões da janela do jogo em pixels. Aqui, definimos as
        # dimensões comuns para um jogo estilo Pac-Man.
LARGURA, ALTURA = 448, 496

# 'pygame.display.set_mode()' configura a janela do display e retorna
        # uma superfície que representa a janela visível.
# A variável 'tela' agora representa essa superfície.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# 'pygame.display.set_caption()' define o título da janela do
        # jogo, que aparece na barra de título da janela.
pygame.display.set_caption("Pac-Man")

# 'pygame.time.Clock()' cria um objeto relógio que pode ser usado
        # para controlar a taxa de atualizações do jogo,
        # também conhecido como quadros por segundo (FPS).
relogio = pygame.time.Clock()

# Define cores usando o modelo RGB, onde cada cor é uma tupla
        # de três valores (R, G, B) que representam,
        # respectivamente, a intensidade do vermelho, verde e azul.
PRETO = (0, 0, 0)       # Cor preta, ausência de cor em RGB.
AZUL = (33, 33, 255)     # Cor azul com máxima intensidade de azul e um pouco de vermelho e verde.
AMARELO = (255, 255, 0)  # Cor amarela, máxima intensidade de vermelho e verde, sem azul.
BRANCO = (255, 255, 255) # Cor branca, máxima intensidade de vermelho, verde e azul.
VERMELHO = (255, 0, 0)   # Cor vermelha, máxima intensidade de vermelho.
ROSA = (255, 182, 193)   # Cor rosa, com intensidades específicas de vermelho, verde e azul.
CIANO = (0, 255, 255)    # Cor ciano, máxima intensidade de verde e azul.
LARANJA = (255, 165, 0)  # Cor laranja, alta intensidade de vermelho com um pouco de verde.

# Carrega uma fonte do sistema para usar no jogo. 'SysFont' pega 
        # uma fonte do sistema e define o tamanho da fonte.
# Aqui, 'arial' é o tipo de fonte escolhida e 24 é o tamanho da fonte.
fonte = pygame.font.SysFont('arial', 24)


# Labirintos para cada fase
labirintos = [
    [
        # Cada string representa uma linha do labirinto na fase 1.
        # 'X' representa paredes que o Pac-Man não pode atravessar.
        # '.' representa os pequenos pontos que o Pac-Man coleta
                # para ganhar pontos.
        # 'o' representa as pastilhas energéticas que permitem ao Pac-Man
                # comer os fantasmas temporariamente.
        # '@' pode representar a localização inicial dos fantasmas ou um 
                # lugar especial no labirinto (não utilizado em todos os jogos).
        # ' ' (espaço em branco) é o caminho por onde o Pac-Man e os
                # fantasmas podem se mover.
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "X............XX............X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X......XX....XX....XX......X",
        "XXXXXX.XXXXX XX XXXXX.XXXXXX",
        "     X.XXXXX XX XXXXX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXX--XXX XX.X     ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "      .   X      X   .      ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "     X.XX XXX--XXX XX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXXXXXXX XX.X     ",
        "XXXXXX.XX XXXXXXXX XX.XXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "X...XX................XX...X",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "X......XX....XX....XX......X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X............@@............X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ],
    # Fase 2
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "X.XXXX................XXXX.X",
        "X............XX............X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X......XX....XX....XX......X",
        "XXXXXX.XXXXX.XX.XXXXX.XXXXXX",
        "     X.XXXXX XX XXXXX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXX--XXX XX.X     ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "      .   X      X   .      ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "     X.XX XXX--XXX XX.X     ",
        "     X.XX          XX.X     ",
        "X....X.XX XXXXXXXX XX.X....X",
        "XoXX.X.XX XXXXXXXX XX.X.XXoX",
        "XoXX....................XXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXX....................XXoX",
        "X...XX................XX...X",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "X......XX....XX....XX......X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X............@@............X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ],
    # Fase 3
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX................XXXXoX",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "X............XX............X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X......XX....XX....XX......X",
        "XXXXXX.XXXXX.XX.XXXXX.XXXXXX",
        "     X.XXXXX XX XXXXX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXX--XXX XX.X     ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "      .   X      X   .      ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "     X.XX XXX--XXX XX.X     ",
        "     X.XX          XX.X     ",
        "X....X.XX XXXXXXXX XX.X....X",
        "XoXX.X.XX XXXXXXXX XX.X.XXoX",
        "XoXX....................XXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXX....................XXoX",
        "X...XX................XX...X",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "X......XX....XX....XX......X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X............@@............X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
]

# Constante que define o tamanho de cada bloco do labirinto em pixels. 
# Essa medida é utilizada para dimensionar paredes e caminhos no jogo.
TAMANHO_BLOCO = 16

# Variável global para manter a pontuação total do jogador durante o jogo.
pontuacao_total = 0

# Define uma função chamada 'carregar_pontuacao_acumulada' 
        # que não recebe parâmetros.
def carregar_pontuacao_acumulada():
    
    # Checa se um arquivo chamado 'pontuacoes.txt' existe no 
            # mesmo diretório do script.
    if os.path.exists("pontuacoes.txt"):
    
        # Abre o arquivo 'pontuacoes.txt' no modo de leitura ('r') e o
                # associa a uma variável chamada 'arquivo'.
        with open("pontuacoes.txt", "r") as arquivo:
        
            # Lê todas as linhas do arquivo e as armazena na lista 'linhas'.
            linhas = arquivo.readlines()
            
            # Inicializa uma variável 'total' com 0, que será usada para
                    # somar todas as pontuações.
            total = 0
            
            # Itera sobre cada 'linha' na lista 'linhas'.
            for linha in linhas:
                
                try:
                    
                    # Tenta executar o código dentro do bloco 'try'.
                    # Remove espaços em branco do começo e fim da string e
                            # divide a string pelo caractere ':'.
                    # Pega o segundo elemento resultante dessa divisão (índice 1), 
                            # que deve ser a pontuação,
                            # e converte esse elemento para inteiro.
                    pontos = int(linha.strip().split(":")[1])
                    
                    # Adiciona o valor convertido para inteiro à variável 'total'.
                    total += pontos
                    
                except:
                    
                    # Se ocorrer algum erro durante a tentativa, o bloco 'except' é executado,
                            # e o 'continue' faz com que o laço pule para a próxima iteração.
                    continue
                    
            # Retorna o valor de 'total' após terminar o loop.
            return total
            
    else:
        
        # Se o arquivo 'pontuacoes.txt' não existir, retorna 0.
        return 0


# Define a função 'mostrar_menu', que exibe o menu inicial do jogo e
        # aceita a pontuação acumulada como argumento.
def mostrar_menu(pontuacao_acumulada):
    
    # Inicia um loop infinito que continuará mostrando o menu até que
            # seja interrompido por uma ação (como pressionar uma tecla).
    while True:
    
        # Preenche toda a superfície da tela com a cor preta
                # para limpar a tela anterior.
        tela.fill(PRETO)
        
        # Renderiza o texto 'Pac-Man' usando a fonte previamente 
                # definida, com a cor amarela.
        titulo = fonte.render('Pac-Man', True, AMARELO)
        
        # Renderiza as instruções 'Pressione ESPAÇO para jogar' 
                # usando a fonte definida, com a cor branca.
        instrucoes = fonte.render('Pressione ESPAÇO para jogar', True, BRANCO)
        
        # Renderiza o texto mostrando a 'Pontuação Acumulada' do jogador, 
                # que é atualizada conforme o valor passado à função.
        pontuacao_texto = fonte.render(f'Pontuação Acumulada: {pontuacao_acumulada}', True, BRANCO)
        
        # Posiciona o texto do título no centro da tela, ajustado 
                # verticalmente para cima em 50 pixels da metade.
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ALTURA // 2 - 50))
        
        # Posiciona o texto de instruções exatamente no centro da tela.
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA // 2))
        
        # Posiciona o texto de pontuação acumulada no centro da tela,
                # ajustado verticalmente para baixo em 50 pixels da metade.
        tela.blit(pontuacao_texto, (LARGURA // 2 - pontuacao_texto.get_width() // 2, ALTURA // 2 + 50))
        
        # Atualiza a tela para mostrar todas as novas informações renderizadas.
        pygame.display.flip()

        
        # Inicia um loop para processar eventos que são capturados pelo Pygame.
        for evento in pygame.event.get():
            
            # Verifica cada evento capturado na fila de eventos do Pygame.
            
            # Verifica se o tipo do evento é QUIT, que é disparado quando o 
                    # usuário clica no botão de fechar a janela.
            if evento.type == pygame.QUIT:
                
                # Chama pygame.quit() para finalizar todos os módulos do
                        # Pygame de maneira adequada.
                pygame.quit()
                
                # Chama sys.exit() para encerrar o programa.
                sys.exit()
            
            # Verifica se o tipo do evento é KEYDOWN, que verifica se 
                    # qualquer tecla foi pressionada.
            if evento.type == pygame.KEYDOWN:
                
                # Dentro do evento KEYDOWN, verifica se a tecla pressionada é 
                        # a barra de espaço (K_SPACE).
                if evento.key == pygame.K_SPACE:
                    
                    # Retorna do método ou função, efetivamente saindo do
                            # loop de menu ou de evento.
                    return



