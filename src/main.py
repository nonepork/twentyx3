from threading import Thread

from countdown import draw_timer
from notify import notify
from state import TimerState
from tray import create_tray


def main_loop(state: TimerState):
    while not state.exit_event.is_set():
        if not draw_timer(5, False, state):
            state.exit_event.wait(1200)
            continue

        draw_timer(20, True, state)

        state.exit_event.wait(1200)


def run():
    state = TimerState()
    notify("twentyx3 started!")
    main_thread = Thread(target=main_loop, args=(state,), daemon=True)
    main_thread.start()
    icon = create_tray(state, main_thread)
    icon.run()


if __name__ == "__main__":
    run()
