import pygame
from .constants import DARK_GREY, WHITE, WIDTH, BLACK, LIGHT_GREY, GREEN, ALPHABET, RED, YELLOW
pygame.init()

FONT = pygame.font.Font('C:/Users/kimba/wordlegame/wordle/HelveticaNeue-Medium-11.ttf', 45)
SUBFONT = pygame.font.Font('C:/Users/kimba/wordlegame/wordle/HelveticaNeue-Medium-11.ttf', 24)

class Board:
    def draw_entry_box(WIN, color, entry_field, x, y):
        pygame.draw.rect(WIN, color, [y * 85 + 10, x * 85 + 10, 75, 75], 0, 4)
        piece_text = FONT.render(entry_field[x][y], True, WHITE)
        WIN.blit(piece_text, (y * 85 + 35, x * 85 + 20))

    def draw_grid(WIN, entry_field):
        WIN.fill(DARK_GREY)
        for y in range(0, 5):
            for x in range(0, 6):
                color = LIGHT_GREY
                Board.draw_entry_box(WIN, color, entry_field, x, y)
        for col in range(10):
            pygame.draw.rect(WIN, LIGHT_GREY, [col * 40 + 20, 525, 35, 45], 0, 4)
            alphabet_text = SUBFONT.render(ALPHABET[0][col], True, WHITE)
            text_rect = alphabet_text.get_rect(center=((30 + 40 * col) + 6, 545))
            WIN.blit(alphabet_text, text_rect)
        for col in range(9):
            pygame.draw.rect(WIN, LIGHT_GREY, [col * 40 + 40, 585, 35, 45], 0, 4)
            alphabet_text = SUBFONT.render(ALPHABET[1][col], True, WHITE)
            text_rect = alphabet_text.get_rect(center=((30 + 40 * col) + 26, 605))
            WIN.blit(alphabet_text, text_rect)
        for col in range(7):
            pygame.draw.rect(WIN, LIGHT_GREY, [col * 40 + 80, 645, 35, 45], 0, 4)
            alphabet_text = SUBFONT.render(ALPHABET[2][col], True, WHITE)
            text_rect = alphabet_text.get_rect(center=((30 + 40 * col) + 66, 665))
            WIN.blit(alphabet_text, text_rect)

    def draw_play_again(WIN):
        pygame.draw.rect(WIN, DARK_GREY, [WIDTH // 2 - 250, 510, 500, 200])
        play_again = SUBFONT.render("Press SPACE to play again", True, WHITE)
        WIN.blit(play_again, (70, 570))
        quit_game = SUBFONT.render("Press ENTER to quit game", True, WHITE)
        WIN.blit(quit_game, (70, 595))

    def draw_game_win(WIN):
        pygame.draw.rect(WIN, BLACK, [WIDTH // 2 - 75, 260 - 25, 150, 50], 0, 4)
        win_text = SUBFONT.render("Good Job", True, GREEN)
        WIN.blit(win_text, (WIDTH // 2 - 55, 260 - 15))
        Board.draw_play_again(WIN)

    def draw_game_loss(WIN, real_word):
        pygame.draw.rect(WIN, RED, [WIDTH // 2 - 75, 260 - 25, 150, 50], 0, 4)
        win_text = SUBFONT.render(real_word.rstrip(real_word[-1]), True, WHITE)
        WIN.blit(win_text, (WIDTH // 2 - 32, 260 - 16))
        Board.draw_play_again(WIN)

    def draw_invalid_input(WIN):
        pygame.draw.rect(WIN, WHITE, [WIDTH // 2 - 150, 260 - 25, 300, 50], 0, 4)
        not_word = SUBFONT.render("Not a Word", True, BLACK)
        WIN.blit(not_word, (WIDTH // 2 - 55, 260 - 15))

    def draw_indicator(WIN, color, z, row, shift):
        pygame.draw.rect(WIN, color, [z * 40 + shift, (525 + 60 * row), 35, 45], 0, 4)
        alphabet_text = SUBFONT.render(ALPHABET[row][z], True, WHITE)
        text_rect = alphabet_text.get_rect(center=((16 + 40 * z) + shift, 545 + 60 * row))
        WIN.blit(alphabet_text, text_rect)

    def indicator_color(WIN, entry_field, turn, real_word_index, x, y, z, row, shift):
        if (entry_field[x][y] == real_word_index[y] == str(ALPHABET[row][z]).lower()) and turn > x:
            color = GREEN
            Board.draw_indicator(WIN, color, z, row, shift)
        elif ((entry_field[x][y] in real_word_index) and entry_field[x][y] == str(ALPHABET[row][z]).lower()) and (turn > x):
            color = YELLOW
            Board.draw_indicator(WIN, color, z, row, shift)
        elif (entry_field[x][y] == str(ALPHABET[row][z]).lower()) and (turn > x):
            color = BLACK
            Board.draw_indicator(WIN, color, z, row, shift)