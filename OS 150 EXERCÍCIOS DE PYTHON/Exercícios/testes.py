import pygame

pygame.init()

# Configuração da janela do jogo
tamanho_janela = (800, 600)
janela = pygame.display.set_mode(tamanho_janela)

# Cor do fundo
cor_fundo = (0, 0, 0)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Lógica do jogo

    # Renderização da tela
    janela.fill(cor_fundo)

    # Desenhar elementos do HUD
    # Exemplo: texto
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render("HUD do Jogo", True, (255, 255, 255))
    janela.blit(texto, (10, 10))

    pygame.display.flip()

pygame.quit()
