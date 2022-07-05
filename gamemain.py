import pygame
import random
from Assets.constants import WIDTH, HEIGHT, GREEN, YELLOW, WHITE, BLACK
from Assets.UI import Board, FONT
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle Unlimited")


def word_exists(words_list, guess, entry_field, turn):
    if turn > 0:
        turn -= 1
        guess[turn] = entry_field[turn][0] + entry_field[turn][1] + \
            entry_field[turn][2] + entry_field[turn][3] + entry_field[turn][4]
        if any(guess[turn] in word for word in words_list):
            return True
        else:
            Board.draw_invalid_input(WIN)
            entry_field[turn] = [" ", " ", " ", " ", " "]
            return False


def letters_used(entry_field, turn, word_in_dict, real_word):
    real_word_index = list(real_word)
    if word_in_dict == True:
        for y in range(0, 5):
            for x in range(0, 6):
                for z in range(10):
                    row, shift = 0, 20
                    Board.indicator_color(
                        WIN, entry_field, turn, real_word_index, x, y, z, row, shift)
                for z in range(9):
                    row, shift = 1, 40
                    Board.indicator_color(
                        WIN, entry_field, turn, real_word_index, x, y, z, row, shift)
                for z in range(7):
                    row, shift = 2, 80
                    Board.indicator_color(
                        WIN, entry_field, turn, real_word_index, x, y, z, row, shift)


def letter_check(real_word, entry_field, turn, guess, word_in_dict):
    game_won = False
    real_word_index = list(real_word)
    if word_in_dict == True:
        for y in range(0, 5):
            for x in range(0, 6):
                guess[x] = entry_field[x][0] + entry_field[x][1] + \
                    entry_field[x][2] + entry_field[x][3] + entry_field[x][4]
                if (guess[x] in real_word) and (turn > x):
                    color = GREEN
                    Board.draw_entry_box(WIN, color, entry_field, x, y)
                    Board.draw_game_win(WIN)
                    game_won = True
                elif entry_field[x][y] == real_word_index[y] and turn > x:
                    color = GREEN
                    Board.draw_entry_box(WIN, color, entry_field, x, y)
                elif entry_field[x][y] in real_word_index and turn > x:
                    color = YELLOW
                    Board.draw_entry_box(WIN, color, entry_field, x, y)
                elif entry_field[x][y] not in real_word_index and turn > x:
                    color = BLACK
                    Board.draw_entry_box(WIN, color, entry_field, x, y)
        return game_won


def main():
    words = open("C:/Users/kimba/wordguess/five_letters.csv")
    words_list = []
    for row in words:
        transformed_row = row.replace(",", "")
        words_list.append(transformed_row)
    real_word = words_list[random.randint(1, len(words_list))]
    words.close()
    print(real_word)

    entry_field = [[" ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " "]]

    FPS = 60
    run = True
    clock = pygame.time.Clock()
    letters = turn = 0
    continue_word = True
    game_over = False
    word_in_dict = True
    guess = [[], [], [], [], [], []]
    while run:
        clock.tick(FPS)
        Board.draw_grid(WIN, entry_field)
        letters_used(entry_field, turn, word_in_dict, real_word)
        game_over = letter_check(
            real_word, entry_field, turn, guess, word_in_dict)
        word_in_dict = word_exists(words_list, guess, entry_field, turn)

        if turn == 6 and word_in_dict == True and not(guess[turn - 1] in real_word):
            game_over = True
            continue_word = False
            Board.draw_game_loss(WIN, real_word)
        if letters == 5:
            continue_word = False
        if letters < 5:
            continue_word = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and letters > 0:
                    entry_field[turn][letters - 1] = " "
                    letters -= 1
                if word_in_dict == False:
                    turn -= 1
                    letters = 0
                elif event.key == pygame.K_RETURN and letters == 5:
                    turn += 1
                    letters = 0
                    word_exists(words_list, guess, entry_field, turn)
                if event.key == pygame.K_RETURN and game_over:
                    run = False
                if event.key == pygame.K_SPACE and game_over:
                    main()
            if event.type == pygame.TEXTINPUT and continue_word == True and turn < 6:
                entry = event.__getattribute__('text')
                entry_field[turn][letters] = entry.lower()
                letters += 1
        pygame.display.update()
    pygame.quit()
    exit()


main()
