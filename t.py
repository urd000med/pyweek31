import math
import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
player = pygame.transform.smoothscale(pygame.image.load("arrow_up.png").convert_alpha(), (100, 100))

correction_angle = 90

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player_pos  = window.get_rect().center
    player_rect = player.get_rect(center = player_pos)

    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

    rot_image      = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center = player_rect.center)

    window.fill((255, 255, 255))
    window.blit(rot_image, rot_image_rect.topleft)
    pygame.display.flip()

pygame.quit()
exit()
