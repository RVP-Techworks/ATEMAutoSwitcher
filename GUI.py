import tkinter as tk
from startup_manager import is_open_at_startup

class GUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()  # Pack this frame into the parent
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.ip_label = tk.Label(self, text="ATEM IP Address:")
        self.ip_label.pack(pady=5)

        self.ip_entry = tk.Entry(self)
        self.ip_entry.pack(pady=5)

        self.timer_label = tk.Label(self, text="Timer Interval (seconds):")
        self.timer_label.pack(pady=5)

        self.timer_entry = tk.Entry(self)
        self.timer_entry.insert(0, str(self.parent.timer_interval))
        self.timer_entry.pack(pady=5)

        self.connect_button = tk.Button(self, text="Connect", command=self.parent.toggle_connection)
        self.connect_button.pack(pady=5)

        self.status_label = tk.Label(self, text="")
        self.status_label.pack(pady=5)

        self.checkbox_frame = tk.Frame(self)
        self.checkbox_frame.pack(pady=10)

        self.create_checkboxes(8)

        self.countdown_label = tk.Label(self, text="", fg="red")
        self.countdown_label.pack(pady=5)

    def create_menu(self):
        menubar = tk.Menu(self.parent)  # Attach the menu to the parent (tk.Tk instance)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.parent.save_configuration)  # Updated to correct method name
        filemenu.add_command(label="Load", command=self.parent.load_config_from_file)
        self.parent.open_at_startup_var = tk.BooleanVar(value=is_open_at_startup())
        filemenu.add_checkbutton(label="Open at startup", onvalue=True, offvalue=False, variable=self.parent.open_at_startup_var, command=self.parent.toggle_open_at_startup)
        menubar.add_cascade(label="File", menu=filemenu)

        viewmenu = tk.Menu(menubar, tearoff=0)
        self.parent.show_timer_var = tk.BooleanVar(value=True)
        viewmenu.add_checkbutton(label="Show Timer", onvalue=True, offvalue=False, variable=self.parent.show_timer_var, command=self.parent.toggle_timer)
        self.parent.show_console_var = tk.BooleanVar(value=False)
        menubar.add_cascade(label="View", menu=viewmenu)

        self.parent.config(menu=menubar)

    def create_checkboxes(self, num_inputs):
        self.parent.checkboxes = []  # Initialize the checkboxes list in the parent
        for i in range(1, num_inputs + 1):
            var = tk.BooleanVar(value=True)  # Default to checked
            checkbox = tk.Checkbutton(self.checkbox_frame, text=f"Input {i}", variable=var)
            checkbox.pack(anchor="w")
            self.parent.checkboxes.append((i, var))  # Add to parent's checkboxes list

