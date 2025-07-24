import pygame
import win32con
import win32gui

from src.state import TimerState

pygame.font.init()

SMALL_FONT = pygame.font.SysFont("comicsans", 100)
BIG_FONT = pygame.font.SysFont("comicsans", 250)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (30, 30, 30)


def set_always_on_top():
    win32gui.SetWindowPos(
        pygame.display.get_wm_info()["window"],
        win32con.HWND_TOPMOST,
        0,
        0,
        0,
        0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
    )


def init_window(big=False):
    if big:
        win = pygame.display.set_mode((0, 0))
        width, height = win.get_size()
        half_width, half_height = width / 2, height / 2
        font = BIG_FONT
    else:
        win = pygame.display.set_mode((150, 150), pygame.NOFRAME)
        half_width, half_height = 75, 75
        font = SMALL_FONT
    set_always_on_top()
    return win, half_width, half_height, font


def draw_handler(win, timer, timer_pos):
    win.fill(DARK_GRAY)
    win.blit(timer, timer_pos)
    pygame.display.update()


def draw_timer(seconds, big, state: TimerState):
    win, half_width, half_height, font = init_window(big)
    clock = pygame.time.Clock()
    last_tick = pygame.time.get_ticks()

    timer = font.render(str(seconds), True, LIGHT_GRAY)
    half_timer_width, half_timer_height = timer.get_size()
    timer_pos = [half_width - half_timer_width / 2, half_height - half_timer_height / 2]

    draw_handler(win, timer, timer_pos)

    state.running = True

    while state.running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                if state.gamer_enabled:
                    state.running = False

        now = pygame.time.get_ticks()

        if now - last_tick >= 1000:
            last_tick = now
            seconds -= 1

            if seconds == 0:
                break

            timer = font.render(str(seconds), True, LIGHT_GRAY)
            timer_pos[0] = half_width - timer.get_width() / 2
            draw_handler(win, timer, timer_pos)

    pygame.display.quit()
    return state.running
