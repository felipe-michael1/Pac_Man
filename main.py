# importar as classes para o main

from pacman import carregar_pontuacao_acumulada
from pacman import mostrar_menu
from pacman import pygame
from pacman import random
from pacman import sys

from pacman import labirintos

from pacman import TAMANHO_BLOCO
from pacman import LARGURA
from pacman import ALTURA
from pacman import BRANCO
from pacman import VERMELHO
from pacman import ROSA
from pacman import CIANO
from pacman import LARANJA
from pacman import PRETO
from pacman import AZUL
from pacman import AMARELO

from jogador import Jogador
from ponto import Ponto
from pastilha import Pastilha
from fantasma import Fantasma

from pacman import relogio
from pacman import tela
from pacman import labirintos
from pacman import fonte
# Define a função 'main', que é o ponto de entrada principal do jogo.
def main():
    
    # Declara 'pontuacao_total' como uma variável global, permitindo
            # que ela seja modificada dentro da função.
    global pontuacao_total

    # Inicia um loop infinito que continuará rodando o jogo até
            # ser explicitamente encerrado.
    while True:
    
        # Chama a função 'carregar_pontuacao_acumulada' para obter a
                # pontuação acumulada de sessões anteriores.
        pontuacao_acumulada = carregar_pontuacao_acumulada()
        
        # Exibe o menu inicial do jogo, passando a pontuação 
                # acumulada para ser mostrada.
        mostrar_menu(pontuacao_acumulada)
        
        # Inicializa a variável 'fase_atual' com 0, indicando o
                # início do jogo na primeira fase.
        fase_atual = 0
        
        # Reinicializa 'pontuacao_total' com 0 para começar a contagem 
                # de pontos para a nova sessão de jogo.
        pontuacao_total = 0
        
        # Define 'vidas' com 5, dando ao jogador 5 vidas no início do jogo.
        vidas = 5


        # Inicia um loop que continua enquanto 'fase_atual' for menor 
                # que o número total de labirintos disponíveis.
        while fase_atual < len(labirintos):
            
            # Cria listas vazias para armazenar objetos de paredes, 
                    # pontos, pastilhas e fantasmas.
            paredes = []
            pontos = []
            pastilhas = []
            fantasmas = []
        
            # Seleciona o labirinto correspondente à fase atual 
                    # da lista de labirintos.
            labirinto = labirintos[fase_atual]
        
            # Determina o número de linhas no labirinto, que é o número de
                    # elementos na lista labirinto.
            LINHAS = len(labirinto)
            
            # Determina o número de colunas no labirinto, que é o comprimento do
                    # primeiro elemento (string) da lista labirinto.
            COLUNAS = len(labirinto[0])
        
            # Define a posição inicial do jogador dentro do labirinto.
            # Multiplica-se o número de bloco padrão pelo índice para centralizar o 
                    # jogador no meio do labirinto na vertical e próxima ao 
                    # centro na horizontal.
            jogador_posicao_inicial = (14 * TAMANHO_BLOCO, 23 * TAMANHO_BLOCO)
            
            # Cria uma instância do jogador na posição inicial definida.
            jogador = Jogador(*jogador_posicao_inicial)


            # Cria o labirinto iterando sobre cada linha e cada coluna dentro 
                    # do array de strings do labirinto.
            for linha in range(LINHAS):
                
                for coluna in range(COLUNAS):
                    
                    # Acessa o caractere específico no labirinto que indica o 
                            # tipo de bloco (parede, ponto, etc.)
                    bloco = labirinto[linha][coluna]
                    
                    # Calcula a posição x baseada na coluna atual, multiplicando
                            # pelo tamanho padrão do bloco.
                    x = coluna * TAMANHO_BLOCO
                    
                    # Calcula a posição y baseada na linha atual, também multiplicando
                            # pelo tamanho do bloco.
                    y = linha * TAMANHO_BLOCO
                    
                    # Verifica se o caractere no labirinto é 'X', o que
                            # indica uma parede.
                    if bloco == 'X':
                    
                        # Cria um retângulo na posição calculada que servirá 
                                # como uma parede no jogo.
                        parede = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)
                        
                        # Adiciona o retângulo criado à lista de paredes.
                        paredes.append(parede)
                        
                    # Verifica se o caractere é '.', indicando um ponto coletável.
                    elif bloco == '.':
                        
                        # Cria um objeto Ponto na posição calculada.
                        ponto = Ponto(x, y)
                        
                        # Adiciona o ponto à lista de pontos que o jogador pode coletar.
                        pontos.append(ponto)
                        
                    # Verifica se o caractere é 'o', indicando uma pastilha.
                    elif bloco == 'o':
                        
                        # Cria um objeto Pastilha na posição calculada.
                        pastilha = Pastilha(x, y)
                        
                        # Adiciona a pastilha à lista de pastilhas, que são 
                                # itens especiais no jogo.
                        pastilhas.append(pastilha)
                        
                    # Verifica se o caractere é '@', indicando a posição 
                            # inicial de um fantasma.
                    elif bloco == '@':
                        
                        # Cria um objeto Fantasma na posição calculada e
                                # define sua cor como vermelho.
                        fantasma = Fantasma(x, y, VERMELHO)
                        
                        # Adiciona o fantasma criado à lista de fantasmas 
                                # que irão perseguir o jogador.
                        fantasmas.append(fantasma)


            # Define a variável 'numero_de_fantasmas_extra' com 
                    # base no número da fase atual.
            # Multiplica o índice da fase atual por 2 para aumentar a
                    # dificuldade progressivamente:
            # Na primeira fase (índice 0), não adiciona fantasmas extras.
            # Na segunda fase (índice 1), adiciona 2 fantasmas 
                    # extras, e assim por diante.
            numero_de_fantasmas_extra = fase_atual * 2  # 0 na primeira fase, 2 na segunda, etc.
            
            # Lista das cores disponíveis para os fantasmas extras.
            # Isso permite variar visualmente os fantasmas e pode também 
                    # indicar diferentes comportamentos ou propriedades.
            cores_fantasmas = [VERMELHO, ROSA, CIANO, LARANJA]
            
            # Define posições iniciais para os fantasmas extras.
            # Essas posições são estrategicamente escolhidas para estar no
                    # centro do labirinto, facilitando a distribuição dos fantasmas.
            posicoes_fantasmas = [
                (14 * TAMANHO_BLOCO, 14 * TAMANHO_BLOCO),  # Posição central.
                (14 * TAMANHO_BLOCO, 15 * TAMANHO_BLOCO),  # Posição abaixo do centro.
                (13 * TAMANHO_BLOCO, 14 * TAMANHO_BLOCO),  # Posição à esquerda do centro.
                (15 * TAMANHO_BLOCO, 14 * TAMANHO_BLOCO)   # Posição à direita do centro.
            ]


            # Inicializa uma lista vazia para armazenar as posições
                    # iniciais dos fantasmas adicionais.
            fantasmas_posicoes_iniciais = []
            
            # Itera sobre o número de fantasmas extras determinado 
                    # pela fase atual do jogo.
            for i in range(numero_de_fantasmas_extra):
                
                # Seleciona a posição para o novo fantasma usando um padrão 
                        # circular com base no número total de posições disponíveis.
                # Isso assegura que a lista de posições não seja excedida,
                        # reutilizando posições conforme necessário.
                x, y = posicoes_fantasmas[i % len(posicoes_fantasmas)]
                
                # Seleciona a cor para o novo fantasma usando um padrão 
                        # circular semelhante ao das posições.
                # Isso garante variação nas cores dos fantasmas adicionais e
                        # evita exceder o número de cores disponíveis.
                cor = cores_fantasmas[i % len(cores_fantasmas)]
                
                # Cria uma nova instância do fantasma na posição e cor determinadas.
                fantasma = Fantasma(x, y, cor)
                
                # Adiciona o novo fantasma à lista de fantasmas ativos no jogo.
                fantasmas.append(fantasma)
                
                # Adiciona a posição inicial do novo fantasma à lista de posições iniciais.
                # Isso é útil para redefinir os fantasmas às suas posições
                        # originais se necessário, por exemplo, após o 
                        # jogador perder uma vida.
                fantasmas_posicoes_iniciais.append((x, y))


            # Inicializa ou reinicializa a lista que armazena as posições 
                    # iniciais de todos os fantasmas.
            # Isso inclui tanto os fantasmas adicionados na fase atual 
                    # quanto qualquer fantasma já existente.
            for fantasma in fantasmas:
                
                # Adiciona a posição atual de cada fantasma na 
                        # lista 'fantasmas_posicoes_iniciais'.
                # Isso é usado para redefinir a posição dos fantasmas caso o
                        # jogador perca uma vida ou reinicie a fase.
                fantasmas_posicoes_iniciais.append((fantasma.posicao[0], fantasma.posicao[1]))
            
            # Inicializa a pontuação da fase atual como zero.
            # Isso garante que a pontuação comece do zero a cada nova fase.
            pontuacao = 0
            
            # Define a variável 'rodando' como True para iniciar o loop 
                    # principal do jogo para a fase.
            # Essa variável controla se o loop de jogo continua executando, 
                    # sendo útil para terminar o jogo ou avançar de fase.
            rodando = True

            # Mantém o jogo executando enquanto a variável 'rodando'
                    # estiver definida como True.
            while rodando:
                
                # Define a taxa de quadros por segundo (FPS) para 60, o que 
                        # significa que o jogo tentará atualizar 60 vezes por segundo.
                relogio.tick(60)  # Limita a 60 FPS
                
                # Itera sobre todos os eventos que ocorreram desde a 
                        # última atualização.
                for evento in pygame.event.get():
                    
                    # Verifica se o evento é do tipo QUIT, que ocorre 
                            # quando o jogador fecha a janela do jogo.
                    if evento.type == pygame.QUIT:
                    
                        # Finaliza todos os módulos do Pygame de maneira adequada.
                        pygame.quit()
                        
                        # Sai do programa completamente.
                        sys.exit()
                    
                    # Verifica se algum evento de tecla pressionada foi capturado.
                    if evento.type == pygame.KEYDOWN:
                        
                        # Verifica se a tecla pressionada é a seta para esquerda.
                        if evento.key == pygame.K_LEFT:
                        
                            # Atualiza a direção desejada do jogador para esquerda.
                            jogador.direcao_desejada = [-1, 0]
                        
                        # Verifica se a tecla pressionada é a seta para direita.
                        elif evento.key == pygame.K_RIGHT:
                            
                            # Atualiza a direção desejada do jogador para direita.
                            jogador.direcao_desejada = [1, 0]
                            
                        # Verifica se a tecla pressionada é a seta para cima.
                        elif evento.key == pygame.K_UP:
                            
                            # Atualiza a direção desejada do jogador para cima.
                            jogador.direcao_desejada = [0, -1]
                            
                        # Verifica se a tecla pressionada é a seta para baixo.
                        elif evento.key == pygame.K_DOWN:
                            
                            # Atualiza a direção desejada do jogador para baixo.
                            jogador.direcao_desejada = [0, 1]


                # Chama o método 'mover' do objeto jogador, passando a 
                        # lista de paredes como argumento.
                # Este método atualiza a posição do jogador com base em sua
                        # direção desejada e verifica colisões.
                jogador.mover(paredes)
                
                # Chama o método 'comer_ponto' do jogador para verificar se o
                        # jogador coletou algum dos pontos no labirinto.
                # O método retorna a quantidade de pontos ganhos, que por
                        # padrão é 1 por ponto coletado.
                # A pontuação retornada é então adicionada à pontuação 
                        # total do jogador para esta fase.
                pontuacao += jogador.comer_ponto(pontos)
                
                # Similar ao método 'comer_ponto', o método 'comer_pastilha' 
                        # verifica se o jogador coletou alguma pastilha.
                # Cada pastilha coletada vale 50 pontos, e esse valor é 
                        # adicionado à pontuação total.
                # As pastilhas geralmente oferecem ao jogador vantagens 
                        # temporárias, como poder comer os fantasmas.
                pontuacao += jogador.comer_pastilha(pastilhas)


                # Itera sobre cada fantasma na lista de fantasmas para 
                        # mover e verificar colisões.
                for idx, fantasma in enumerate(fantasmas):
                    
                    # Chama o método 'mover' do objeto fantasma, passando a
                            # lista de paredes como argumento.
                    # Este método permite que o fantasma se mova dentro do labirinto e 
                            # mude de direção se necessário ao colidir com uma parede.
                    fantasma.mover(paredes)
                    
                    # Verifica se há colisão entre o retângulo de colisão do 
                            # fantasma e o retângulo do jogador.
                    if fantasma.retangulo.colliderect(jogador.retangulo):
                        
                        # Caso haja colisão, significa que o jogador foi "pego" pelo fantasma.
                        # Reduz o número de vidas do jogador em 1.
                        vidas -= 1
                        
                        # Verifica se o jogador ainda tem vidas restantes após ser pego.
                        if vidas > 0:
                            
                            # Se o jogador ainda tem vidas, reinicia a posição do 
                                    # jogador para a posição inicial da fase.
                            # Isso é feito para dar ao jogador a chance de continuar
                                    # jogando a partir de um ponto seguro.
                            jogador.posicao = list(jogador_posicao_inicial)
                            
                            # Reseta a direção atual e a direção desejada do jogador
                                    # para zero, parando seu movimento.
                            jogador.direcao = [0, 0]
                            jogador.direcao_desejada = [0, 0]
                            
                            # Atualiza a posição do retângulo de colisão do jogador para
                                    # corresponder à posição inicial.
                            jogador.retangulo.topleft = jogador.posicao

                            # Reinicia posições dos fantasmas
                            for idx, fantasma in enumerate(fantasmas):
                               
                                # Recupera as posições iniciais dos fantasmas da lista 
                                        # que armazena essas informações.
                                x, y = fantasmas_posicoes_iniciais[idx]
                                
                                # Redefine a posição do fantasma para a sua posição inicial.
                                fantasma.posicao = [x, y]
                                
                                # Atribui uma nova direção aleatória ao fantasma para
                                        # aumentar a imprevisibilidade após o reinício.
                                fantasma.direcao = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
                                
                                # Atualiza o retângulo de colisão do fantasma para
                                        # corresponder à nova posição.
                                fantasma.retangulo.topleft = fantasma.posicao
                            
                            # Exibe mensagem de perda de vida
                            # Preenche toda a tela com a cor preta para limpar o 
                                        # conteúdo anterior.
                            tela.fill(PRETO)
                            
                            # Renderiza uma mensagem informando ao jogador que ele
                                    # perdeu uma vida e mostrando quantas vidas restam.
                            texto_vida = fonte.render(f'Você perdeu uma vida! Vidas restantes: {vidas}', True, BRANCO)
                            
                            # Posiciona a mensagem de perda de vida no centro da tela.
                            tela.blit(texto_vida, (LARGURA // 2 - texto_vida.get_width() // 2, ALTURA // 2))
                            
                            # Atualiza a tela para exibir a mensagem de perda de vida.
                            pygame.display.flip()
                            
                            # Pausa o jogo por 2000 milissegundos (2 segundos) para 
                                    # dar tempo ao jogador de ler a mensagem.
                            pygame.time.wait(2000)

                        else:
                            
                            # Este bloco é executado se o jogador não tiver mais vidas
                                    # restantes, indicando o fim do jogo.
                            
                            # Preenche toda a tela com a cor preta para preparar a 
                                    # exibição da mensagem de fim de jogo.
                            tela.fill(PRETO)
                            
                            # Renderiza a mensagem de fim de jogo usando a cor branca.
                            texto_fim = fonte.render('Você perdeu todas as vidas! Fim de Jogo!', True, BRANCO)
                            
                            # Posiciona a mensagem de fim de jogo no centro da tela.
                            tela.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, ALTURA // 2))
                            
                            # Atualiza a tela para exibir a mensagem de fim de jogo.
                            pygame.display.flip()
                            
                            # Pausa o jogo por 3000 milissegundos (3 segundos) para permitir 
                                    # que o jogador leia a mensagem de fim de jogo.
                            pygame.time.wait(3000)
                            
                            # Adiciona a pontuação obtida na fase atual à pontuação
                                    # total acumulada ao longo do jogo.
                            pontuacao_total += pontuacao
                            
                            # Chama a função para salvar a pontuação total no sistema de
                                    # arquivos ou base de dados conforme implementado.
                            salvar_pontuacao(pontuacao_total)
                            
                            # Define a variável 'rodando' como False para sair do
                                    # loop principal do jogo.
                            rodando = False
                            
                            # Utiliza 'break' para sair imediatamente do loop, retornando ao
                                    # menu principal ou encerrando a fase.
                            break


                # Verifica se a variável 'rodando' foi definida como False, o que 
                        # indica que o jogo deve parar.
                if not rodando:
                
                    # O jogador perdeu todas as vidas e a condição do jogo para 
                            # continuar rodando não é mais verdadeira,
                            # então o loop de jogo é interrompido e controla o
                            # retorno ao menu principal.
                    break
                
                # Verifica se todos os pontos e pastilhas no labirinto
                        # foram coletados pelo jogador.
                if not pontos and not pastilhas:
                    
                    # Adiciona a pontuação obtida na fase atual à
                            # pontuação total acumulada.
                    pontuacao_total += pontuacao
                    
                    # Incrementa a variável 'fase_atual' para mover o
                            # jogo para a próxima fase.
                    fase_atual += 1
                    
                    # Interrompe o loop atual para reiniciar o jogo com a próxima fase,
                    # permitindo que o setup inicial da nova fase seja processado.
                    break
                
                # Prepara a tela para a nova renderização, preenchendo-a com preto.
                # Isso limpa a tela de qualquer desenho anterior antes de
                        # começar a renderizar os novos elementos.
                tela.fill(PRETO)


                # Desenha o labirinto
                for parede in paredes:
                    
                    # Usa a função 'draw.rect' do Pygame para desenhar 
                            # cada parede na tela.
                    # As paredes são desenhadas na cor azul, e cada 'parede' é 
                            # um retângulo definido anteriormente.
                    pygame.draw.rect(tela, AZUL, parede)
                
                # Desenha os pontos
                for ponto in pontos:
                    
                    # Chama o método 'desenhar' da classe Ponto para cada
                            # ponto na lista de pontos.
                    # Este método é responsável por desenhar o ponto na
                            # tela, como definido na classe Ponto.
                    ponto.desenhar(tela)
                
                # Desenha as pastilhas
                for pastilha in pastilhas:
                    
                    # Chama o método 'desenhar' da classe Pastilha para cada
                            # pastilha na lista de pastilhas.
                    # Semelhante ao método da classe Ponto, ele desenha a 
                            # pastilha na tela na posição especificada.
                    pastilha.desenhar(tela)
                
                # Desenha o jogador
                # Chama o método 'desenhar' da classe Jogador para
                        # desenhar o jogador na tela.
                # Este método trata de renderizar o jogador na sua posição
                        # atual e com a aparência definida.
                jogador.desenhar(tela)


                # Desenha os fantasmas
                for fantasma in fantasmas:
                    
                    # Chama o método 'desenhar' da classe Fantasma para cada 
                            # fantasma na lista de fantasmas.
                    # Este método é responsável por renderizar o fantasma na tela, 
                            # utilizando as características definidas na classe Fantasma.
                    fantasma.desenhar(tela)
                
                # Desenha a pontuação
                # Renderiza o texto da pontuação usando a fonte definida, o valor é a 
                        # soma da pontuação total com a pontuação acumulada na fase atual.
                texto_pontuacao = fonte.render(f'Pontuação: {pontuacao_total + pontuacao}', True, BRANCO)

                # Posiciona o texto da pontuação na tela, especificamente no 
                        # canto superior esquerdo a 10 pixels das bordas.
                tela.blit(texto_pontuacao, (10, 10))
                
                # Desenha as vidas
                # Renderiza o texto das vidas restantes do jogador, também 
                        # usando a fonte definida.
                texto_vidas = fonte.render(f'Vidas: {vidas}', True, BRANCO)

                # Posiciona o texto das vidas no canto superior direito da tela, 
                        # ajustando para que não sobreponha a borda.
                tela.blit(texto_vidas, (LARGURA - texto_vidas.get_width() - 10, 10))
                
                # Atualiza a tela para exibir todos os elementos gráficos que 
                        # foram renderizados neste ciclo de jogo.
                pygame.display.flip()


            # Verifica se a variável 'rodando' está definida como False e
                        # se o jogador não possui mais vidas.
            if not rodando and vidas == 0:
                
                # Se ambas as condições forem verdadeiras, indica que o 
                        # jogador perdeu todas as vidas.
                # O loop das fases é interrompido, saindo assim do jogo 
                        # ou retornando ao menu inicial.
                break
            
            # Verifica se o índice da fase atual é menor que o número total de 
                    # labirintos e se o jogador ainda possui vidas.
            if fase_atual < len(labirintos) and vidas > 0:
                
                # Se o jogador concluiu a fase e ainda tem vidas, prepara a
                        # tela para a mensagem de conclusão.
                
                # Preenche a tela com preto para limpar qualquer conteúdo visual anterior.
                tela.fill(PRETO)
                
                # Renderiza o texto 'Fase Concluída!' usando a fonte definida, na cor branca.
                texto_fase = fonte.render('Fase Concluída!', True, BRANCO)
                
                # Posiciona o texto de conclusão da fase centralizado 
                        # horizontalmente e verticalmente na tela.
                tela.blit(texto_fase, (LARGURA // 2 - texto_fase.get_width() // 2, ALTURA // 2))
                
                # Atualiza a tela para mostrar a mensagem de conclusão da fase.
                pygame.display.flip()
                
                # Pausa o jogo por 2000 milissegundos (2 segundos) para
                        # permitir que o jogador leia a mensagem.
                pygame.time.wait(2000)


        else:
        
            # Esta condição é executada se o jogador completar
                    # todas as fases disponíveis no jogo.
            
            # Preenche a tela com preto para limpar qualquer conteúdo 
                    # visual anterior e preparar para a nova mensagem.
            tela.fill(PRETO)
            
            # Renderiza a mensagem de vitória usando a fonte definida, na cor branca.
            texto_vitoria = fonte.render('Parabéns! Você venceu!', True, BRANCO)
            
            # Renderiza a mensagem de pontuação final, mostrando a 
                    # pontuação total acumulada durante o jogo.
            pontuacao_final = fonte.render(f'Pontuação Total: {pontuacao_total}', True, BRANCO)
            
            # Posiciona o texto de vitória acima do centro
                    # horizontal e vertical da tela.
            tela.blit(texto_vitoria, (LARGURA // 2 - texto_vitoria.get_width() // 2, ALTURA // 2 - 20))
            
            # Posiciona o texto da pontuação final abaixo do centro
                    # horizontal e vertical da tela.
            tela.blit(pontuacao_final, (LARGURA // 2 - pontuacao_final.get_width() // 2, ALTURA // 2 + 20))
            
            # Atualiza a tela para mostrar as mensagens de vitória e
                    # de pontuação final.
            pygame.display.flip()
            
            # Pausa o jogo por 5000 milissegundos (5 segundos) para 
                    # permitir que o jogador leia as mensagens.
            pygame.time.wait(5000)
            
            # Chama a função para salvar a pontuação total no sistema de 
                    # arquivos ou base de dados conforme implementado.
            salvar_pontuacao(pontuacao_total)


# Define a função 'salvar_pontuacao' que recebe um 
        # argumento 'pontuacao'.
def salvar_pontuacao(pontuacao):
    
    # Abre ou cria um arquivo chamado 'pontuacoes.txt' no modo de adição ('a'),
    # que permite escrever no final do arquivo sem 
            # sobrescrever o conteúdo existente.
    with open("pontuacoes.txt", "a") as arquivo:
        
        # Escreve a pontuação recebida no arquivo, formatada 
                # com a etiqueta 'Pontuação: ',
                # seguida pelo valor da pontuação e uma quebra de
                # linha para separar entradas subsequentes.
        arquivo.write(f"Pontuação: {pontuacao}\n")

# Chama a função 'main' para iniciar o jogo.
# Esta é a entrada do programa que dispara a execução de
        # todas as lógicas do jogo.


main()
