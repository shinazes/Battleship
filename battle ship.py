import pygame
import random

from pygame import MOUSEBUTTONDOWN

#------------------------
#constants and settings
#------------------------

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)


WIDTH = 20
HEIGHT = 20
MARGIN = 10

#screen settings
SCREEN_WIDTH = 370
SCREEN_HEIGHT = 400
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

#fonts
font = pygame.font.SysFont('Arial', 20)
font_main = pygame.font.SysFont('Arial', 40)
font_second = pygame.font.SysFont('Arial', 30)

image_path = 'battleship_image.png' #1050px by 514px


#-----------------
# sub-program
#-----------------
#label -> index
def cordinate_index(cordinate):
    if len(cordinate) <2:
        return -1,-1
    letter = cordinate[0]
    number = cordinate[1:]
    row = ord(letter)-ord('A')
    for d in number:
        if not ord('0')<= ord(d)<= ord('9'):
            return -1,-1
    collum = int(number)-1
    return row, collum

 #admin board
def debug_board(b):
    output =' '
    for i in range(len(b[0])):
        output+=' ' + str(i+1)
    print(output)
    for i in range(len(b)):
        output = chr(i+ord('A'))
        for value in b[ i ]:
            output += ' '+str( value )
        print(output)

# generating random positions for ships
def gen_pos(b,size):
    oriantation = random.randint(0,1)

    if oriantation == 0:
        row = random.randint(0,len(b)-1)
        col =  random.randint(0,len(b[0])-size)
    else:
        row = random.randint(0,len(b)-size)
        col =  random.randint(0,len(b[0])-1)
    return row , col, oriantation

#check if the ships colliding
def iscoliding(b,row,col,size,oriantation):
    for off_set in range(size):
        if oriantation == 0:
            if b[row][col+ off_set] != 0:
                return True
        else:
            if b[row + off_set][col] != 0:
                return True
    return False

#placing ships on grid
def place_ship(b,row,col,size,oriantation):
    for off_set in range(size):
        if oriantation == 0:
            b[row][col+off_set] = 1
        else:
            b[row+off_set][col] = 1

#Check if the guess inputed is hit or miss
def guess(b,row,col):
    if not 0<= row <len(b):
        print('Invalid')
        return False
    if not 0<= col<len(b[0]):
        print('Invalid')
        return False
    value =b[row][col]
    if value >1:
        print('Already guess')
        return False
    b[row][col] += 2
    if value == 0:
        print('Miss')
        return False
    else:
        print('Hit')
        return True

ship_size = [2]
tiles_left = 0

done = False
done2 = False
mouse_clicked = False



while not done:
    done2 = False
    #Borads
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    board2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    ship_size = [2] #number and sizes of ships, 1 ship by 2 by deafult
    attempts = 0

    #starting menu
    while not done2:
        #clearing the screen before anything is drawn
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user closes the app than the program stops
                done = True
                done2 = True
            elif event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEBUTTONUP: #checking is there a mouse click
                pos = pygame.mouse.get_pos() #setting the place where mouse has clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True
                    print(pos)
                else:
                    mouse_clicked = False

                if mouse_clicked and pygame.MOUSEBUTTONDOWN and pos[0] >= 116 and pos[0] <= 161 and pos[1] >= 300 and \
                        pos[1] <= 352: # if mouse clicked "<" button them the number of ships whould decrease
                    if len(ship_size) >= 1:
                        ship_size.pop()

                if mouse_clicked and pygame.MOUSEBUTTONDOWN and pos[0] >= 209 and pos[0] <= 254 and pos[1] >= 300 and \
                        pos[1] <= 352: # if mouse clicked the number of ships will add in sizes
                    if len(ship_size) == 0:
                        ship_size.append(2)
                    elif len(ship_size) == 1:
                        ship_size.append(3)
                    elif len(ship_size) >= 2 and len(ship_size) <= 5:
                        ship_size.append(4)

        #draw a battleship image
        image = pygame.image.load(image_path).convert_alpha() #loading the image from the image_path
        scaled_image = pygame.transform.scale(image, (315, 154)) #shrinking the image
        screen.blit(scaled_image, ((SCREEN_WIDTH - 315) // 2, 30)) #drawing the image

        #play button
        if mouse_clicked and pos[0] >= 116 and pos[0] <= 255 and pos[1] >= 187 and pos[1] <= 238: #if mouse clicked then the color of button changes and done changes to True so the while loop finishes
            btn_color = (100, 200, 200)
            btn_bg_color = (70, 70, 70)
            done2 = True
        else:
            btn_color = (255, 255, 255)
            btn_bg_color = (100, 100, 100)

        play_again_text = font_main.render("Play", True, btn_color) # assigning the variable with text and font
        pygame.draw.rect(screen, btn_bg_color, [(SCREEN_WIDTH - 138) // 2, 185, 78 + 60, 50], 0) #drawing the rectangle behind the text
        screen.blit(play_again_text, [(SCREEN_WIDTH - 78) // 2, 185]) #displaying the text

        #number of ships text display
        number_of_ships_text = font_second.render("number of ships", True, WHITE)# assigning the variable with text and font
        screen.blit(number_of_ships_text, [(SCREEN_WIDTH - 226) // 2, 250])

        # left arrow button
        if mouse_clicked and pos[0] >= 116 and pos[0] <= 161 and pos[1] >= 300 and pos[1] <= 352: #if mouse clicked then the color of button changes and done changes to True so the while loop finishes
            btn_color = (100, 200, 200)
            btn_bg_color = (70, 70, 70)
        else:
            btn_color = (255, 255, 255)
            btn_bg_color = (100, 100, 100)

        left_arrow = font_main.render("<", True, btn_color)# assigning the variable with text and font
        pygame.draw.rect(screen, btn_bg_color, [(SCREEN_WIDTH - 138) // 2, 300, 45, 50], 0)#drawing the rectangle behind the text
        screen.blit(left_arrow, [(SCREEN_WIDTH - 115) // 2, 302])#displaying the text

        # Number of ships display
        number_of_ships_number = font_main.render(str(len(ship_size)), True, WHITE)# assigning the variable with text and font
        screen.blit(number_of_ships_number, [(SCREEN_WIDTH - 22) // 2, 302])#displaying the text

        # Right arrow button
        if mouse_clicked and pos[0] >= 209 and pos[0] <= 254 and pos[1] >= 300 and pos[1] <= 352: #if mouse clicked then the color of button changes and done changes to True so the while loop finishes
            btn_color = (100, 200, 200)
            btn_bg_color = (70, 70, 70)
        else:
            btn_color = (255, 255, 255)
            btn_bg_color = (100, 100, 100)

        right_arrow = font_main.render(">", True, btn_color)# assigning the variable with text and font
        pygame.draw.rect(screen, btn_bg_color, [(SCREEN_WIDTH + 48) // 2, 300, 45, 50], 0)#drawing the rectangle behind the text
        screen.blit(right_arrow, [(SCREEN_WIDTH + 71) // 2, 302]) #displaying the text

        #button mechanics



        pygame.display.flip()
        clock.tick(60)
        if done2:
            pygame.time.delay(500)

    #calling functions to create locations and sizes of the ships
    for s in ship_size:
        r, c, o = gen_pos(board, s)
        tiles_left += s
        while iscoliding(board, r, c, s, o):
            r, c, o = gen_pos(board, s)
        place_ship(board, r, c, s, o)

    done2 = False
    debug_board(board) #printing the board with location of ships into the terminal

    # Displaying the game
    while not done2 and tiles_left > 0 and not done:
        # clearing the screen
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT : #Window will close if user closes the game
                done2 = True
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:#user clicks the mouse and getting the input where the click happened
                pos = pygame.mouse.get_pos() #locating where the mouse has clicked
                column = (pos[0] - 40) // (WIDTH + MARGIN) #determining which column has the location of click
                row = (pos[1] - 40) // (HEIGHT + MARGIN )
                if board2[row][column] == 0:
                    attempts += 1
                board2[row][column] = 1
                if board2[row][column] == board[row][column]:
                    tiles_left -= 1
                print("Click ", pos, "Grid coordinates: ", row, column)
                print(tiles_left)


        #outputing the coordinate lables
        for row in range(10):
            text = font.render(chr(65 + row), True, WHITE)# assigning the variable with text and font
            screen.blit(text, (10, 45 + (MARGIN + WIDTH) * row + WIDTH//2 - text.get_width()//2)) #displaying the text

        for column in range(10):
            text = font.render(str(column + 1), True, WHITE) # assigning the variable with text and font
            screen.blit(text, (50 + (MARGIN + HEIGHT) * column + HEIGHT//2 - text.get_height()//2, 10)) #displaying the text


        #drawing the grid and changing colours
        for row in range(10):
            for column in range(10):
                color = WHITE
                if board2[row][column] == 1 and board2[row][column] == board[row][column]: # checks if the tile was hit
                    color = GREEN #tile hit
                elif board2[row][column] == 1:
                    color = YELLOW #tile miss
                pygame.draw.rect(screen,   # creating the grid itself
                                color,
                                [40 + (MARGIN + WIDTH) * column + MARGIN,
                                 40 + (MARGIN + HEIGHT) * row + MARGIN,
                                 WIDTH,
                                 HEIGHT])

        #displaying how many tiles left
        text = font.render("ships left: " + str(tiles_left), True, WHITE) # assigning the variable with text and font
        screen.blit(text, [50, 350, 20, 200]) #displaying the text

        #displaying attempts
        attempts_text = font.render("Attempts:", True, WHITE) # assigning the variable with text and font
        attempts_number = font.render(str(attempts), True, WHITE) # assigning the variable with text and font
        screen.blit(attempts_text, [200, 350]) #displaying the text
        screen.blit(attempts_number, [295, 351]) #displaying the text


        # Screen refresh
        clock.tick(60)
        pygame.display.flip()
        if tiles_left == 0:
            pygame.time.delay(1000)

    done2 = False

    #ending screen
    while not done2 and not done:
        # clearing the screen before end screen is drawn
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT :  #Window will close if user closes the game
                done2 = True
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEBUTTONUP: #user clicks the mouse and getting the input where the click happened
                pos = pygame.mouse.get_pos()  #locating where the mouse has clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True
                    print(pos)
                else:
                    mouse_clicked = False

        #Congratulation print
        congrats = font_main.render("You Win!", True, WHITE) # assigning the variable with text and font
        screen.blit(congrats, [(SCREEN_WIDTH - 159) // 2, 75]) #displaying the text

        #play again button
        if mouse_clicked and pos[0] >= 82 and pos[0] <= 266.5 and pos[1] >= 132.5 and pos[1] <= 162.5:
            btn_color = (00, 200, 200)
            btn_bg_color = (70, 70, 70)
            play_again = True
        else:
            btn_color = (255, 255, 255)
            btn_bg_color = (100, 100, 100)

        play_again_text = font.render("Play Again", True, btn_color) # assigning the variable with text and font
        pygame.draw.rect(screen, btn_bg_color, [82, 132.5, 134, 30], 0) #drawing the rectangle behind the text
        screen.blit(play_again_text, [102, 135]) #displaying the text


        #quit button
        if mouse_clicked and pos[0] >= 82 and pos[0] <= 266.5 and pos[1] >= 182.5 and pos[1] <= 212.5: #if mouse clicked then the color of button changes
            btn_color = RED
            btn_bg_color = (70, 70, 70)
        else:
            btn_color = (255, 255, 255)
            btn_bg_color = (100, 100, 100)

        quit_text = font.render("Quit", True, btn_color) # assigning the variable with text and font
        pygame.draw.rect(screen, btn_bg_color, [82, 182.5, 134, 30], 0) #drawing the rectangle behind the text
        screen.blit(quit_text, [102, 185]) #displaying the text

        #button Mechanics
        if mouse_clicked and pygame.MOUSEBUTTONUP and pos[0] >= 82 and pos[0] <= 266.5 and pos[1] >= 182.5 and pos[1] <= 212.5: # if the quit button pressed the the game closes
            done = True
            done2 = True
        elif mouse_clicked and pygame.MOUSEBUTTONUP and pos[0] >= 82 and pos[0] <= 266.5 and pos[1] >= 132.5 and pos[1] <= 162.5:
            done2 = True

        #screen refresh
        clock.tick(60)
        pygame.display.flip()



pygame.quit()