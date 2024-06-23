import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load(
    'UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load(
    'UltimatePygameIntro-main/graphics/ground.png').convert()

game_over_surf = test_font.render('Game Over', False, 'Black')
game_over_rect = game_over_surf.get_rect(center=(400, 200))

test_surface = test_font.render('Test - Game', False, 'Black')
test_rect = test_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load(
    'UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load(
    'UltimatePygameIntro-main/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

running = True
collision = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 800
                collision = True
                game_active = True

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, 'Pink', test_rect)
        pygame.draw.rect(screen, 'Pink', test_rect, 10)
        # pygame.draw.line(screen, 'Red', (0, 100), (800, 100), width = 10)
        screen.blit(test_surface, test_rect)
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf, player_rect)
        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800
            collision = True

        if player_rect.colliderect(snail_rect) and collision:
            collision = False
            game_active = False

    else:
        screen.blit(game_over_surf, game_over_rect)

    '''
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print("mouse")
    '''

    pygame.display.update()
    clock.tick(60)
