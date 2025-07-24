from threading import Event


class TimerState:
    def __init__(self):
        self.exit_event = Event()
        self.gamer_enabled = False
        self.running = False

    def toggle_gamer(self):
        self.gamer_enabled = not self.gamer_enabled

    def clean_up(self):
        """Safely clean up state and notify listeners, do not change the orders."""
        self.running = False
        if not self.exit_event.is_set():
            self.exit_event.set()
