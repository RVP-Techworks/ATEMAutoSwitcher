import contextlib
import tkinter as tk
from tkinter import filedialog
import random
import io
import sys
from atem_controller import ATEMController
from GUI import GUI
from atem_monitor import monitor_tally
from config_manager import save_config, load_config
from startup_manager import add_to_startup, remove_from_startup, is_open_at_startup
from timer_manager import TimerManager

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATEM Auto Switcher")
        self.geometry("400x450")

        # Initialize variables
        self.config_file = "switcher_ip.txt"
        self.timer_interval = 100  # Default timer interval in seconds
        self.checkboxes = []  # list of tuples (index, tk.BooleanVar)
        self.checkbox_states = {}  # Dictionary of checkbox states
        self.atem_controller = None
        self.countdown = self.timer_interval #initialize countdown

        # Initialize the GUI
        self.gui = GUI(self)

        # Load the configuration
        self.load_configuration()

        # Initialize the timer
        self.timer_manager = TimerManager(self.timer_interval, self.on_timer_expired, self.update_countdown_label)

        # Override the close button
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_configuration(self):
        ip_address, timer_interval, checkboxes_states = load_config(self.config_file)
        
        # Update GUI with loaded configuration
        self.gui.ip_entry.delete(0, tk.END)
        self.gui.ip_entry.insert(0, ip_address)
        self.gui.timer_entry.delete(0, tk.END)
        self.gui.timer_entry.insert(0, str(timer_interval))
        self.timer_interval = timer_interval
        self.checkbox_states = checkboxes_states

        # Update checkboxes
        for index, var in self.checkboxes:
            var.set(self.checkbox_states.get(index, False))

    def save_configuration(self):
        ip_address = self.gui.ip_entry.get()
        timer_interval = int(self.gui.timer_entry.get())
        checkbox_states = {index: var.get() for index, var in self.checkboxes}

        save_config(self.config_file, ip_address, timer_interval, checkbox_states)

    
    def on_timer_expired(self):
        print("Timer expired, switching input")  # Debug statement to ensure this method is called
        selected_inputs = self.get_selected_inputs()
        if selected_inputs:
            random_input = random.choice(selected_inputs)
            print(f"Setting program input with command: PrgI:{random_input}")
            self.atem_controller.switcher.setProgramInputVideoSource(0, random_input)
        self.reset_timer()
        
    def start_timer(self):
        try:
            self.countdown = int(self.gui.timer_entry.get())  # Set countdown based on the timer entry
            self.timer_interval = self.countdown  # Update timer_interval to match the input
            print(f"Timer value set to: {self.countdown}")
        except ValueError:
            self.countdown = self.timer_interval  # Default to last known value if conversion fails
            print(f"Invalid input. Timer set to: {self.countdown}")

        self.timer_manager.interval_seconds = self.countdown
        self.timer_manager.start_timer()



    def stop_timer(self):
        self.timer_manager.stop_timer()

    def reset_timer(self):
        self.countdown = self.timer_interval  # Ensure countdown uses the updated timer_interval
        print(f"Resetting timer to: {self.countdown} seconds")
        self.timer_manager.interval_seconds = self.countdown  # Update timer manager's interval
        self.timer_manager.reset_timer()


    def toggle_connection(self):
        if self.atem_controller and getattr(self.atem_controller.switcher, 'connected', False):
            self.disconnect_from_atem()
        else:
            self.connect_to_atem()

    def connect_to_atem(self):
        ip_address = self.gui.ip_entry.get()
        self.atem_controller = ATEMController()
        if self.atem_controller.connect(ip_address):
            self.gui.status_label.config(text="Connected successfully!", fg="green")
            self.gui.connect_button.config(text="Disconnect")
            self.save_configuration()
            self.start_timer()
            monitor_tally(self.atem_controller, self.reset_timer)
        else:
            self.gui.status_label.config(text="Failed to connect.", fg="red")

    def disconnect_from_atem(self):
        if self.atem_controller and self.atem_controller.switcher:
            self.atem_controller.disconnect()
            self.gui.status_label.config(text="Disconnected.", fg="red")
            self.gui.connect_button.config(text="Connect")
            self.atem_controller = None
            self.stop_timer()

    def set_timer_interval(self, interval):
        self.timer_interval = interval

    def set_saved_checkbox_states(self, states):
        self.saved_checkbox_states = states

    def update_checkboxes(self):
        for i, var in self.checkboxes:
            if i in self.saved_checkbox_states:
                var.set(self.saved_checkbox_states[i])

    def load_config_from_file(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            self.config_file = filename
            self.load_configuration()

    def get_selected_inputs(self):
        return [i for i, var in self.checkboxes if var.get()]

    def update_countdown_label(self, initial=False):
        if not initial and self.countdown > 0:
            self.countdown -= 1  # Decrement countdown only after the first display
        self.gui.countdown_label.config(text=f"Next switch in: {self.countdown+1} seconds")
        self.gui.countdown_label.pack()  # Ensure the label is shown

    def toggle_timer(self):
        self.update_countdown_label()

    def toggle_open_at_startup(self):
        if self.open_at_startup_var.get():
            add_to_startup()
        else:
            remove_from_startup()
        self.update_startup_checkmark()

    def on_close(self):
        """Gracefully close the application"""
        self.stop_timer()
        self.disconnect_from_atem()
        self.destroy()

    def update_startup_checkmark(self):
        self.open_at_startup_var.set(is_open_at_startup())

    # Context manager for capturing console output
    @contextlib.contextmanager
    def capture_console_output(self):
        new_output = io.StringIO()
        old_output = sys.stdout
        try:
            sys.stdout = new_output
            yield new_output
        finally:
            sys.stdout = old_output

if __name__ == "__main__":
    app = Application()
    app.mainloop()
