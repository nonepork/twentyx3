from threading import Thread

from src.countdown import draw_timer
from src.notify import notify
from src.state import TimerState
from src.tray import create_tray

__version__ = "1.0.0"


def main_loop(state: TimerState):
    primed = False
    while not state.exit_event.is_set():
        if primed:
            if not draw_timer(5, False, state):
                state.exit_event.wait(1200)
                continue

            draw_timer(20, True, state)
        else:
            primed = True

        state.exit_event.wait(1200)


def run():
    state = TimerState()
    notify("twentyx3 started!")
    main_thread = Thread(target=main_loop, args=(state,), daemon=True)
    main_thread.start()
    icon = create_tray(state, main_thread)
    icon.run()
