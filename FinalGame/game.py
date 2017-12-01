# encoding: utf-8
# coded by Jordan, date: 301117, start time: 10:48, end time: ##:##

import pygame, random

# --- UNIVERSAL VARIABLES
title = "Run Bogo, Run!"
# ----------
screen_width = 800
screen_height = 600
# ----------
half_width = screen_width // 2
half_height = screen_height // 2
# ----------
white =     (255, 255, 255)
gray =      (180, 180, 180)
black =     (0, 0, 0)
# ----------
images = []
for index in range(12):
    images.append("images/red-50/red" + str(index) + ".png")
images_ram = []
for index in range(8):
    images_ram.append("images/ram-50/ram" + str(index) + ".png")

class wall(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start, width, height, color):         # Función constructor
        super().__init__()                                              # Esta función llama al constructor padre

        self.image = pygame.Surface([width, height])
        self.image.fill(color)


        self.rect = self.image.get_rect()
        self.rect.y = y_start
        self.rect.x = x_start

class red(pygame.sprite.Sprite):
    x_speed_force = 0
    y_speed_force = 0

    def __init__(self, x, y, list):
        super().__init__()

        self.image = pygame.image.load(list[1])

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def change_image(self, index, list):
        self.image = pygame.image.load(list[index])

    def change_speed_force(self, x, y):
        self.x_speed_force += x
        self.y_speed_force += y

    def move(self, walls):
        self.rect.x += self.x_speed_force

        collision_blocks = pygame.sprite.spritecollide(self, walls, False)
        for block in collision_blocks:
            if self.x_speed_force > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.y_speed_force

        collision_blocks = pygame.sprite.spritecollide(self, walls, False)
        for block in collision_blocks:
            if self.y_speed_force > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class map():

    wall_list = None
    enemys = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()

class first_map(map):
    def __init__(self):
        super().__init__()

        walls = [
                # border walls
                [0,     0,      50,     600, white],        # l
                [750,   0,      100,    500, white],        # l
                [750,   700,    50,     50,  white],        # .
                [50,    0,      750,    50,  white],        # -
                [50,    550,    800,    50,  white],        # -
                # inside walls
                [100, 100, 50, 100, white],
                [50, 300, 100, 50, white],
                [100, 250, 50, 50, white],
                [150, 100, 150, 50, white],
                [350, 50,  50, 200, white],
                [200, 200, 50, 150, white],
                [650, 300, 50, 200, white],
                [550, 450, 50, 100, white],
                [500, 350, 150, 50, white],
                [400, 350, 50, 200, white],
                [300, 450, 200, 50, white],
                [250, 200, 50, 50, white],
                [100, 400, 150, 50, white],
                [250, 300, 100, 50, white],
                [100, 450, 50, 50, white],
                [200, 500, 50, 50, white],
                [300, 400, 50, 50, white],
                [400, 200, 50, 100, white],
                [500, 200, 50, 150, white],
                [450, 100, 150, 50, white],
                [550, 150, 50, 50, white],
                [650, 50, 50, 50, white],
                [650, 150, 100, 50, white],
                [600, 250, 100, 50, white],
                ]
        for item in walls:
            wall_ta = wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall_ta)

class second_map(map):
    def __init__(self):
        super().__init__()

        walls = [
                    [0,     0,      50,  500,    white],
                    [0,     550,    800,  600,   white],
                    [50,    0,      750, 50,     white],
                    [750,   50,     100,  100,   white],
                    [750,   350,    100,  300,   white],
                ]

        for item in walls:
            wall_ta = wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall_ta)

class third_map(map):
    def __init__(self):
        super().__init__()

        walls = [
                    [0, 0, 50, 150, white],
                    [0, 350, 50, 250, white],
                    [50, 0, 800, 50, white],
                    [750, 50, 50, 600, white],
                    [50, 550, 750, 50, white],
                    [0, 0, 0, 0, white],
                    [0, 0, 0, 0, white]
                 ]

        for item in walls:
            wall_ta = wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall_ta)

def change_spriteImage(sprite, index, list):
    sprite.change_image(index, list)

def button_sprite_loader(imagefile, x_rect, y_rect):
    image_sprite = pygame.image.load(imagefile + ".png")
    image_sprite_hover = pygame.image.load(imagefile + "_hover.png")
    sprite = pygame.sprite.Sprite()
    sprite.image = image_sprite
    sprite.rect = image_sprite.get_rect()
    sprite.rect.left = x_rect
    sprite.rect.top = y_rect

    return sprite, image_sprite, image_sprite_hover

def hover_loader(list, xPos_mouse, yPos_mouse):
    for i in range(len(list)):
        x, y, width, height = list[i][0].rect
        if (xPos_mouse >= x and xPos_mouse <= x + width) and (yPos_mouse >= y and yPos_mouse <= y + height):
            list[i][0].image = list[i][2]
        else:
            list[i][0].image = list[i][1]

def click_detector(list, xPos_mouse, yPos_mouse):
    for i in range(len(list)):
        x, y, width, height = list[i][0]
        if (xPos_mouse >= x and xPos_mouse <= x + width) and (yPos_mouse >= y and yPos_mouse <= y + height):
            return list[i][1]

def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption(title)

    red_p = red(50 , 50, images)
    move_sprites = pygame.sprite.Group()
    move_sprites.add(red_p)

    # --- BUTTON LOADER WITH FUNCTION ---
    # --- main menu
    play_button, image_play_button, image_play_button_hover = button_sprite_loader("images/menu/menu_play_button", 58, 10)
    high_button, image_high_button, image_high_button_hover = button_sprite_loader("images/menu/high_button", 58, 305)
    htp_button, image_htp_button, image_htp_button_hover = button_sprite_loader("images/menu/htp_button", 58, 400)
    choose_button, image_choose_button, image_choose_button_hover = button_sprite_loader("images/menu/choose_button", 58, 495)
    # ---- highscore
    return_button, image_return_button, image_return_button_hover = button_sprite_loader("images/menu/return_button", 26, 490)
    # ---- choose
    choose_red, image_red, image_red_hover = button_sprite_loader("images/menu/choose_red", 50, 50)
    choose_ram, image_ram, image_ram_hover = button_sprite_loader("images/menu/choose_ram", 425, 50)
    # --- LIST LOADER FOR HOVERING, AND CLICKING
    menu_sprites = []
    menu_sprites.append([play_button, image_play_button, image_play_button_hover])
    menu_sprites.append([high_button, image_high_button, image_high_button_hover])
    menu_sprites.append([htp_button, image_htp_button, image_htp_button_hover])
    menu_sprites.append([choose_button, image_choose_button, image_choose_button_hover])
    # ---
    click_list = []
    click_list.append([play_button.rect, "game"])
    click_list.append([high_button.rect, "highscore"])
    click_list.append([htp_button.rect, "htp"])
    click_list.append([choose_button.rect, "choose"])
    # ---
    highscore_sprites = []
    highscore_sprites.append([return_button, image_return_button, image_return_button_hover])
    click_high = []
    click_high.append([return_button.rect, "menu"])
    # ---
    choose_sprites = []
    choose_sprites.append([choose_red, image_red, image_red_hover])
    choose_sprites.append([choose_ram, image_ram, image_ram_hover])


    # --- MUSIC LOADER ------------------
    music_theme = pygame.mixer.Sound("music/theme.wav")
    walking = pygame.mixer.Sound("music/walking.wav")
    click = pygame.mixer.Sound("music/click.wav")
    pygame.mixer.Sound.play(music_theme)

    # --- MAP LOADER --------------------
    maps = []

    maps.append(first_map())
    maps.append(second_map())
    maps.append(third_map())

    actual_map_not = 0
    actual_map = maps[actual_map_not]
    # ------------------------------------

    clock = pygame.time.Clock()
    points = 0
    done = False

    state = "menu"
    final_images = ""

    while not done:

        for event in pygame.event.get():
            xPos_mouse, yPos_mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True


            down = [0, 2]
            right = [3, 5]
            left = [6, 8]
            up = [9, 11]
            if final_images == "red":
                red_l = 6
                red_r = 5
                red_u = 11
                red_d = 2
                list_to_use = images
                static_l = 7
                static_r = 4
                static_u = 10
                static_d = 1

            elif final_images == "ram":
                red_l = 3
                red_r = 7
                red_u = 1
                red_d = 5
                list_to_use = images_ram
                static_l = 2
                static_r = 6
                static_u = 0
                static_d = 7
            else:
                red_l = 6
                red_r = 5
                red_u = 11
                red_d = 2
                list_to_use = images
                static_l = 7
                static_r = 4
                static_u = 10
                static_d = 1

            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(walking)
                if event.key == pygame.K_LEFT:
                    change_spriteImage(red_p, red_l, list_to_use)
                    red_p.change_speed_force(-5, 0)

                if event.key == pygame.K_RIGHT:
                    change_spriteImage(red_p, red_r, list_to_use)
                    red_p.change_speed_force(5, 0)

                if event.key == pygame.K_UP:
                    change_spriteImage(red_p, red_u, list_to_use)
                    red_p.change_speed_force(0, -5)

                if event.key == pygame.K_DOWN:
                    change_spriteImage(red_p, red_d, list_to_use)
                    red_p.change_speed_force(0, 5)


            if event.type == pygame.KEYUP:
                pygame.mixer.Sound.stop(walking)
                if event.key == pygame.K_LEFT:
                    change_spriteImage(red_p, static_l, list_to_use)
                    red_p.change_speed_force(5, 0)
                if event.key == pygame.K_RIGHT:
                    change_spriteImage(red_p, static_r, list_to_use)
                    red_p.change_speed_force(-5, 0)
                if event.key == pygame.K_UP:
                    change_spriteImage(red_p, static_u, list_to_use)
                    red_p.change_speed_force(0, 5)
                if event.key == pygame.K_DOWN:
                    change_spriteImage(red_p, static_d, list_to_use)
                    red_p.change_speed_force(0, -5)

        red_p.move(actual_map.wall_list)

        if red_p.rect.x < -15:
            if actual_map_not == 0:
                actual_map_not = 2
                actual_map = maps[actual_map_not]
                red_p.rect.x = 790

            elif actual_map_not == 2:
                actual_map_not = 1
                actual_map = maps[actual_map_not]
                red_p.rect.x = 790
            else:
                actual_map_not = 0
                actual_map = maps[actual_map_not]
                red_p.rect.x = 790

        if red_p.rect.x > 801:
            if actual_map_not == 0:
                actual_map_not = 1
                actual_map = maps[actual_map_not]
                red_p.rect.x = 0
            elif actual_map_not == 1:
                actual_map_not = 2
                actual_map = maps[actual_map_not]
                red_p.rect.x = 0
            else:
                actual_map_not = 0
                actual_map = maps[actual_map_not]
                red_p.rect.x = 0


        screen.fill(black)


        if state == "menu":

            # --- LOAD BACKGROUND
            background = pygame.image.load("images/menu/menu_background.png")
            screen.blit(background, (0, 0))

            # --- LOAD 1ST BUTTON
            screen.blit(play_button.image, play_button.rect)
            screen.blit(high_button.image, high_button.rect)
            screen.blit(htp_button.image, htp_button.rect)
            screen.blit(choose_button.image, choose_button.rect)

            # --- FULL BLOCK HOVER CONDITION ------
            hover_loader(menu_sprites, xPos_mouse, yPos_mouse)
            # -------------------------------------

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(click)
                pygame.mixer.Sound.play(click)
                state = click_detector(click_list, xPos_mouse, yPos_mouse)
            else:
                state = "menu"

        elif state == "game":
            # pygame.mixer.Sound.stop(music_theme)

            actual_map.wall_list.draw(screen)
            background = pygame.image.load("maps/map1.png")
            screen.blit(background, (0, 0))
            move_sprites.draw(screen)

        elif state == "highscore":

            background = pygame.image.load("images/menu/menu_background.png")
            screen.blit(background, (0, 0))
            screen.blit(return_button.image, return_button.rect)

            hover_loader(highscore_sprites, xPos_mouse, yPos_mouse)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(click)
                x, y, width, height = return_button.rect
                if (xPos_mouse >= x and xPos_mouse <= x + width) and (yPos_mouse >= y and yPos_mouse <= y + height):
                    state = "game"
        elif state == "choose":

            background = pygame.image.load("images/menu/menu_background.png")
            screen.blit(background, (0, 0))
            screen.blit(choose_red.image, choose_red.rect)
            screen.blit(choose_ram.image, choose_ram.rect)

            hover_loader(choose_sprites, xPos_mouse, yPos_mouse)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(click)
                x_r, y_r, r_width, r_height = choose_red.rect
                x_d, y_d, d_width, d_height = choose_ram.rect
                if (xPos_mouse >= x_r and xPos_mouse <= x_r + r_width) and (yPos_mouse >= y_r and yPos_mouse <= y_r + r_height):
                    final_images = "red"
                    state = "game"
                if (xPos_mouse >= x_d and xPos_mouse <= x_d + d_width) and (yPos_mouse >= y_d and yPos_mouse <= y_d + d_height):
                    final_images = "ram"
                    state = "game"

        elif state == "htp":

            background = pygame.image.load("images/menu/menu_background.png")
            screen.blit(background, (0, 0))
            screen.blit(return_button.image, return_button.rect)
            htp_block, htp_image_block, htp_image_block_hover = button_sprite_loader("images/menu/htp_block", 58, 10)
            screen.blit(htp_block.image, htp_block.rect)
            hover_loader(highscore_sprites, xPos_mouse, yPos_mouse)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(click)
                x, y, width, height = return_button.rect
                if (xPos_mouse >= x and xPos_mouse <= x + width) and (yPos_mouse >= y and yPos_mouse <= y + height):
                    state = "game"



        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()