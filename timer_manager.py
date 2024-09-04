import threading

class TimerManager:
    def __init__(self, interval_seconds, on_expire_callback, on_update_callback):
        self.interval_seconds = interval_seconds
        self.on_expire_callback = on_expire_callback
        self.on_update_callback = on_update_callback
        self.timer = None
        self.is_running = False

    def start_timer(self):
        self.stop_timer()  # Ensure any previous timer is stopped
        self.is_running = True
        self.on_update_callback(initial=True)  # Show the initial value
        self._start_countdown()

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()
        self.is_running = False

    def reset_timer(self):
        print("Timer reset")
        self.start_timer()

    def _start_countdown(self):
        if self.interval_seconds > 0:
            self.interval_seconds -= 1
            self.on_update_callback()  # Update the countdown label every second
            self.timer = threading.Timer(1, self._start_countdown)  # Call every second
            self.timer.start()
        else:
            self.timer_expired()

    def timer_expired(self):
        print("Timer expired, executing callback")
        self.is_running = False
        self.on_expire_callback()
