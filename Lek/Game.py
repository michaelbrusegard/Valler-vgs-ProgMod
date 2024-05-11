import pygame

pygame.init()
window = pygame.display.set_mode((910, 540))
pygame.display.set_caption("BLOCK SMASH")
z = 20
y = 120
x = 60
vel = 5
clock = pygame.time.Clock()
fps_limit = 60

run = True
while run:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.QUIT:
            run_me = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 10
        window.fill((0,0,0))
        pygame.draw.circle(window, (255, 0, 0), (x, y), z)
        pygame.display.flip()

pygame.quit()