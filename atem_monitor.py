import time
from threading import Thread

def monitor_tally(atem_controller, reset_timer_callback):
    def monitor():
        while True:
            if not atem_controller or not atem_controller.switcher or not atem_controller.switcher.connected:
                break

            current_src = atem_controller.switcher.programInput[0].videoSource.value

            if current_src != atem_controller.last_src:
                print(f"Tally {current_src} [ON]" if current_src == atem_controller.last_src else f"Tally {current_src} [OFF]")
                atem_controller.last_src = current_src
                reset_timer_callback()

            time.sleep(0.01)  # Reduce CPU usage with a sleep interval

    tally_thread = Thread(target=monitor, daemon=True)
    tally_thread.start()
