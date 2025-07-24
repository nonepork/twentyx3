import pygame
from PIL import Image
from pystray import Icon
from pystray import Menu
from pystray import MenuItem

from src.state import TimerState


def create_tray(state: TimerState, main_thread):
    icon = Icon(
        "twentyx3",
        Image.open("src/assets/icon.png"),
        "twentyx3",
        menu=Menu(
            MenuItem(
                "Gamer mode",
                lambda icon, item: state.toggle_gamer(),
                checked=lambda item: state.gamer_enabled,
            ),
            MenuItem("Exit", lambda icon, item: exit_app(icon, state, main_thread)),
        ),
    )
    return icon


def exit_app(icon, state, main_thread):
    """
    Exits the entire app,
    not sure if I should put it in here or not
    """
    state.clean_up()
    main_thread.join()
    icon.stop()
    pygame.quit()
