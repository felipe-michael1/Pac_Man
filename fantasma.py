from pacman import random
from pacman import pygame
from pacman import TAMANHO_BLOCO
from pacman import LARGURA

# Define a classe 'Fantasma', que representa os inimigos no jogo.
class Fantasma:
    
    # Método construtor que inicializa um novo fantasma com
            # coordenadas x e y e uma cor específica.
    def __init__(self, x, y, cor):
    
        # Armazena a posição inicial do fantasma como uma lista
                # de duas coordenadas [x, y].
        self.posicao = [x, y]
        
        # Define a direção inicial do fantasma escolhendo aleatoriamente
                # entre as quatro possíveis direções.
        # Isso é feito usando 'random.choice', que seleciona um
                # item aleatório de uma lista.
        self.direcao = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
        
        # Define a velocidade do fantasma. Neste caso, é um valor
                # constante de 2, igual à velocidade do jogador.
        self.velocidade = 2
        
        # Cria um retângulo de colisão para o fantasma. O retângulo é 
                # posicionado na localização inicial
                # e tem o tamanho de 'TAMANHO_BLOCO', que é o 
                # tamanho padrão para os elementos do jogo.
        self.retangulo = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        # Armazena a cor do fantasma, que é usada para desenhá-lo na
                # tela. A cor é passada como parâmetro.
        self.cor = cor

    
    def mover(self, paredes):
        
        # Calcula a nova posição do fantasma baseando-se na direção
                # atual e na velocidade.
        nova_posicao = [self.posicao[0] + self.direcao[0] * self.velocidade,
                        self.posicao[1] + self.direcao[1] * self.velocidade]
        
        # Cria um novo retângulo para essa posição, usado para 
                # detectar colisões com as paredes.
        novo_retangulo = pygame.Rect(nova_posicao[0], nova_posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        # Verifica se há colisão entre o novo retângulo e qualquer uma das paredes.
        if not self.verificar_colisao(novo_retangulo, paredes):
            
            # Se não houver colisão, atualiza a posição do 
                    # fantasma para a nova posição.
            self.posicao = nova_posicao
            
            # Atualiza o retângulo de colisão do fantasma para a nova posição.
            self.retangulo = novo_retangulo
            
        else:
            
            # Se houver colisão, o fantasma escolhe uma nova direção
                    # aleatoriamente para tentar evitar a parede.
            self.direcao = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
    
        # Verifica se o fantasma passa pelos limites laterais do mapa,
                # permitindo "teletransporte" de um lado ao outro.
        if self.posicao[0] < -TAMANHO_BLOCO:
            
            # Se o fantasma sai pelo lado esquerdo da tela, ele 
                    # aparece no lado direito.
            self.posicao[0] = LARGURA
            
        elif self.posicao[0] > LARGURA:
            
            # Se o fantasma sai pelo lado direito da tela, ele 
                    # aparece no lado esquerdo.
            self.posicao[0] = -TAMANHO_BLOCO
    
        # Atualiza a posição do retângulo de colisão para estar 
                # alinhado com a nova posição do fantasma.
        self.retangulo.topleft = self.posicao

    
    # Define o método 'verificar_colisao' dentro da classe 'Fantasma'.
    def verificar_colisao(self, retangulo, paredes):
        
        # Este loop passa por cada 'parede' na lista 'paredes'.
        for parede in paredes:
        
            # Usa 'colliderect' para verificar se há uma interseção 
                    # entre o 'retangulo' do fantasma e qualquer 'parede'.
            if retangulo.colliderect(parede):
            
                # Retorna True se uma colisão for detectada, indicando 
                        # que o fantasma não pode mover para essa posição.
                return True
                
        # Retorna False se não houver colisões detectadas, permitindo 
                # que o fantasma continue seu movimento.
        return False
    
    # Define o método 'desenhar' dentro da classe 'Fantasma'.
    def desenhar(self, superficie):
        
        # Utiliza a função 'draw.rect' do pygame para desenhar o 
                # retângulo do fantasma na 'superficie' do jogo.
        pygame.draw.rect(superficie, self.cor, self.retangulo)
        # O retângulo é desenhado usando a cor armazenada em 'self.cor', e
                # as dimensões são definidas em 'self.retangulo'.
