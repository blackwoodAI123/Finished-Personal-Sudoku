#MAKE IT 900 by 900 Pixels 80 px boxes and 5 pixel lines

import pygame
import sys
from board import Board

"""
Checks the position of the mouse
x position of mouse, y position of mouse, x top left corner, y top left corner, x bottom right corner, y bottom right corner
"""
def check_mouse_pos(x_mouse, y_mouse, x_object, y_object, x_object_2, y_object_2):
    if x_mouse >= x_object and x_mouse <= x_object_2 and y_mouse >= y_object and y_mouse <= y_object_2:
        return True
    else:
        return False

#Prints text
def print_text(string, x, y, size, color, is_bold):
    font = pygame.font.SysFont("Times New Roman", size, is_bold, False)
    message = font.render(string, False, color)
    screen.blit(message, (x, y))


#Creates button with arguments
"""
text, position_x, position_y, length, width, size of text, color, and bold
"""
def create_button(button_text, x, y, button_length, button_width, button_color, size, color, is_bold):
    button = pygame.Rect(x, y, button_length, button_width,)
    pygame.draw.rect(screen, button_color, button, 0, 5)
    print_text(button_text, x, y, size, color, is_bold)

"""
Prints sudoku number to screen
NOt setting backend correctly
"""
def print_number(pressed, click_position):
    if pressed[pygame.K_1]:
        value = 1
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_2]:
        value = 2
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_3]:
        value = 3
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_4]:
        value = 4
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_5]:
        value = 5
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_6]:
        value = 6
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_7]:
        value = 7
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_8]:
        value = 8
        board.sketch(value, click_position[0], click_position[1])
    elif pressed[pygame.K_9]:
        value = 9
        board.sketch(value, click_position[0], click_position[1])

    if pressed[pygame.K_RETURN]:
        screen.fill("white")
        board.clear(click_position[0] - 1, click_position[1] - 1)
        board.draw()
        try:
            board.place_number(value, click_position[0] * 80 - 80, click_position[1] * 80 - 80)
            board.update_board(click_position[0] - 1, click_position[1] - 1, value)
        except:
            return True
        return True

    return False


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((880, 900))

    running = True
    while running:

        #24 Frames Per Second
        clock = pygame.time.Clock()
        clock.tick(60)
        no_selection = True
        restart = False

        while no_selection:
            bg = pygame.image.load("BackgroundImage2.png")
            screen.blit(bg, (0, 0))
            print_text("Welcome to Sudoku", 15, 150, 100, (108, 165, 184), True)


            """
            Gets the Mouse Position
            """
            mouse_pos = pygame.mouse.get_pos()


            """
            Button Pictures
            """
            easy_button = create_button("Easy", 220, 550, 100, 60, (255, 165, 0), 50, (0, 255, 0), False)
            medium_button = create_button("Medium", 330, 550, 170, 60, (255, 165, 0), 50, (0, 0, 255), False)
            hard_button = create_button("Hard", 510, 550, 100, 60, (255, 165, 0), 50, (255, 0, 0), False)

            """
            Lightens the color of orange if the mouse is hovering over
            """
            if check_mouse_pos(mouse_pos[0], mouse_pos[1], 220, 550, 320, 610) is True:
                easy_button = create_button("Easy", 220, 550, 100, 60, (255, 213, 128), 50, (0, 255, 0), False)

            elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 330, 550, 500, 610) is True:
                medium_button = create_button("Medium", 330, 550, 170, 60, (255, 213, 128), 50, (0, 0, 255), False)

            elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 510, 550, 610, 610):
                hard_button = create_button("Hard", 510, 550, 100, 60, (255, 213, 128), 50, (255, 0, 0), False)

            pygame.display.update()

            """
            Checks if there is a click in the button region
            """
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    no_selection = False
                    running = False
                    sys.exit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if check_mouse_pos(mouse_pos[0], mouse_pos[1], 220, 550, 330, 610):
                        board = Board(3, 3, screen, 1)
                        no_selection = False

                    elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 330, 550, 500, 610):
                        board = Board(3, 3, screen, 40)
                        no_selection = False


                    elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 510, 550, 610, 610):
                        board = Board(3, 3, screen, 50)
                        no_selection = False


        game_playing = True
        screen.fill("white")
        board.set_sudoku_backend()
        board.set_original_sudoku()
        board.draw()
        click_position = (-1, -1)

        while game_playing:

            if board.is_full():
                game_playing = False
                break

            """
            Gets the Mouse Position
             """
            mouse_pos = pygame.mouse.get_pos()
            pygame.display.update()
            """
            Create Buttons
            """
            reset_button = create_button("Reset", 100, 820, 112, 60,
                                         (255, 165, 0), 50, (0, 255, 0), False)
            restart_button = create_button("Restart", 220, 820, 142, 60,
                                         (255, 165, 0), 50, (0, 255, 0), False)
            exit_button = create_button("Exit", 370, 820, 85, 60,
                                           (255, 165, 0), 50, (0, 255, 0), False)

            """
            Lightens button if mouse is over them
            """
            if check_mouse_pos(mouse_pos[0], mouse_pos[1], 100, 820, 212, 880) is True:
                reset_button = create_button("Reset", 100, 820, 112, 60,
                                             (255, 213, 128), 50, (0, 255, 0), False)
            elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 220, 820, 362, 880) is True:
                restart_button = create_button("Restart", 220, 820, 142, 60,
                                               (255, 213, 128), 50, (0, 255, 0), False)
            elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 370, 820, 455, 880) is True:
                exit_button = create_button("Exit", 370, 820, 85, 60,
                                            (255, 213, 128), 50, (0, 255, 0), False)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_position = board.click(mouse_pos[0], mouse_pos[1])

                    if click_position[0] < 10 and click_position[0] > 0 and click_position[1] < 10 and click_position[1] > 0:
                        board.draw()
                        board.select(click_position[0], click_position[1])

                        no_input = True
                        while no_input is True:
                            mouse_pos = pygame.mouse.get_pos()
                            pressed = pygame.key.get_pressed()
                            x = print_number(pressed, click_position)
                            if x is True:
                                no_input = False
                            pygame.display.update()

                            for ev in pygame.event.get():
                                if ev.type == pygame.MOUSEBUTTONDOWN:
                                    click_position_selected = board.click(mouse_pos[0], mouse_pos[1])
                                    if (click_position_selected[0] != click_position[0] or
                                            click_position_selected[1] != click_position[1]):
                                        no_input = False

                                if ev.type == pygame.QUIT:
                                    pygame.quit()
                                    no_selection = False
                                    running = False
                                    sys.exit()

                    board.draw()
                    """
                    Button Functionality
                    """
                    if check_mouse_pos(mouse_pos[0], mouse_pos[1], 100, 820, 212, 880) is True:
                        board.reset_to_original()
                        screen.fill("white")
                        board.draw()

                    elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 220, 820, 362, 880) is True:
                        game_playing = False
                        restart = True
                    elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 370, 820, 455, 880) is True:
                        pygame.quit()
                        no_selection = False
                        running = False
                        sys.exit()

                #Quits Pygame
                if event.type == pygame.QUIT:
                    pygame.quit()
                    no_selection = False
                    running = False
                    sys.exit()

        if restart == False:
            game_over = True
            screen.fill("white")
            if board.check_board():
                bg = pygame.image.load("WinImage.png")
                win = True
            else:
                bg = pygame.image.load("LoseImage.png")
                win = False
            screen.blit(bg, (0, 0))

            while game_over:
                mouse_pos = pygame.mouse.get_pos()

                """
                Creates buttons of Exit and Restart
                
                Also Lightens button if Mouse is hovering over it
                """
                if win == True:
                    print_text("Game Won!", 200, 400, 100, (0, 0, 0), True)
                    if check_mouse_pos(mouse_pos[0], mouse_pos[1], 400, 550, 485, 610) is True:
                        exit_button = create_button("Exit", 400, 550, 85, 60,
                                                    (255, 213, 128), 50, (0, 0, 0), False)
                    else:
                        exit_button = create_button("Exit", 400, 550, 85, 60,
                                                (255, 165, 0), 50, (0, 0, 0), False)

                else:
                    print_text("Game Over!", 200, 400, 100, (108, 165, 184), True)
                    print_text("You Lose!", 250, 500, 100, (108, 165, 184), True)
                    if check_mouse_pos(mouse_pos[0], mouse_pos[1], 380, 600, 530, 660):
                        exit_button = create_button("Restart", 380, 600, 150, 60,
                                                (255, 213, 128), 50, (0, 0, 0), False)
                    else:
                        exit_button = create_button("Restart", 380, 600, 150, 60,
                                                (255, 165, 0), 50, (0, 0, 0), False)

                pygame.display.update()

                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        game_over = False
                        running = False
                        sys.exit()

                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if check_mouse_pos(mouse_pos[0], mouse_pos[1], 400, 550, 485, 610)\
                                and win is True:
                            pygame.quit()
                            running = False
                            sys.exit()

                        elif check_mouse_pos(mouse_pos[0], mouse_pos[1], 380, 600, 530, 660)\
                                and win is False:
                            game_over = False




