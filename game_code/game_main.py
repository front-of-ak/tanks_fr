# version v1.0.0
import pygame

from game_code import level_generator
from universal_constants import WIDTH, HEIGHT, LEVEL_NAME

pygame.init()

# screen and clock init
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# from sound_init import screens_sound
from game_level_class import GameLevel
from screens import StartScreen, WonScreen, LoseScreen

MAX_LEVEL = 5

# window constants
GAME_TITLE = 'WWII: Величайшие танковые битвы'
pygame.display.set_caption(GAME_TITLE)


class Game:
    def __init__(self, main_screen, main_clock):
        self.screen = main_screen
        self.clock = main_clock
        # self.prev_music = screens_sound

        self.won_screen_run = False
        self.lost_screen_run = False
        self.start_screen_run = True
        self.screen_process(StartScreen)

    def screen_process(self, cur_screen):
        next_screen = None
        if cur_screen == WonScreen:
            cur_screen = WonScreen(self.screen, self.clock)
            next_screen = StartScreen
        elif cur_screen == LoseScreen:
            cur_screen = LoseScreen(self.screen, self.clock)
            next_screen = StartScreen
        elif cur_screen == StartScreen:
            cur_screen = StartScreen(self.screen, self.clock)
            next_screen = GameLevel

        while cur_screen.is_running():
            pass

        if next_screen == GameLevel:
            self.level_process()
        else:
            # self.prev_music = screens_sound
            self.screen_process(next_screen)

    def level_process(self):
        game_level = GameLevel(self.screen, self.clock, level_generator.generate(LEVEL_NAME))
        # self.prev_music = LEVEL_MUSIC[self.current_level]
        player_won = None
        while player_won is None:
            player_won = game_level.is_player_won()
        pygame.mouse.set_visible(True)

        if player_won:
            self.screen_process(WonScreen)
        else:
            self.screen_process(LoseScreen)


Game(screen, clock)
