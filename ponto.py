from pacman import pygame
from pacman import TAMANHO_BLOCO
from pacman import BRANCO

# Define a classe 'Ponto', que representa os pontos
        # coletáveis no jogo.
class Ponto:
    
    # Método construtor que inicializa um novo objeto Ponto com coordenadas x e y.
    def __init__(self, x, y):
        
        # Armazena a posição do ponto como uma lista de duas coordenadas [x, y].
        self.posicao = [x, y]
        
        # Cria um retângulo de colisão para o ponto. Este retângulo é
                # posicionado no centro do bloco
                # com um deslocamento para centralizar um círculo 
                # de 4 pixels de diâmetro (2 pixels de raio).
        self.retangulo = pygame.Rect(x + TAMANHO_BLOCO//2 - 2, y + TAMANHO_BLOCO//2 - 2, 4, 4)
    
    # Método para desenhar o ponto na superfície de jogo especificada.
    def desenhar(self, superficie):
        
        # Desenha um círculo branco na superfície de jogo que 
                # representa o ponto visualmente.
        # O círculo é desenhado no centro do bloco em que o 
                # ponto está posicionado.
        pygame.draw.circle(superficie, BRANCO, (self.posicao[0] + TAMANHO_BLOCO // 2, self.posicao[1] + TAMANHO_BLOCO // 2), 2)
