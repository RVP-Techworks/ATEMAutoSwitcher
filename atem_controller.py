import PyATEMMax
from threading import Thread, Event
import time

class ATEMController:
    def __init__(self):
        self.switcher = None
        self.last_src = None  # To track the last source
        self.stop_event = Event()  # Event to signal thread shutdown

    def connect(self, ip_address):
        print(f"Connecting to {ip_address}...")
        try:
            self.switcher = PyATEMMax.ATEMMax()
            print(f"PyATEMax instanse created"
                  f"\nConnecting to {ip_address}...")
            self.switcher.connect(ip_address)

            # Attempt to connect up to 5 times
            max_tries = 5
            for i in range(max_tries):
                if not self.switcher.connected:
                    print(f"Connection attempt {i+1}/{max_tries} failed. Retrying...")
                    self.switcher.waitForConnection(timeout=5)
                else:
                    break
                  
            if not self.switcher.connected:
                print("Connection failed.")
                return False

            # Start the listener thread for program feed changes
            self.start_program_feed_listener()

            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def start_program_feed_listener(self):
        # Start a thread that continuously checks for program feed changes
        self.stop_event.clear()  # Ensure the stop event is not set
        self.listener_thread = Thread(target=self.program_feed_listener, daemon=True)
        self.listener_thread.start()

    def program_feed_listener(self):
        while self.switcher.connected and not self.stop_event.is_set():
            try:
                current_src = self.switcher.programInput[0].videoSource.value
                if current_src != self.last_src:
                    self.on_program_input_changed(current_src)
                    self.last_src = current_src
                time.sleep(0.1)  # Adjust sleep time as necessary
            except Exception as e:
                print(f"Error in program feed listener: {e}")
                break  # Exit the loop if an error occurs

    def on_program_input_changed(self, source):
        print(f"Program feed changed to input {source}")
        if hasattr(self, 'parent'):
            self.parent.reset_timer()

    def set_program_input(self, input_id):
        try:
            # Set the program input using the correct method
            me_index = 0  # Use the main Mix Effect Block (ME)
            self.switcher.setProgramInputVideoSource(me_index, input_id)
            print(f"Program input set to {input_id}")
        except Exception as e:
            print(f"Error switching program input: {e}")

    def disconnect(self):
        if self.switcher:
            self.stop_event.set()  # Signal the listener thread to stop
            self.listener_thread.join()  # Wait for the listener thread to finish
            self.switcher.disconnect()
            print("Disconnected successfully")
