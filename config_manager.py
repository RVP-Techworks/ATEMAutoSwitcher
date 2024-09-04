import os
import tkinter as tk

def save_config(config_file, ip_address, timer_interval, checkbox_states):
    """
    Save the current configuration to a file.

    :param config_file: The path to the configuration file.
    :param ip_address: The IP address to save.
    :param timer_interval: The timer interval to save.
    :param checkbox_states: A dictionary of checkbox indices and their boolean states.
    """
    with open(config_file, "w", encoding="utf-8") as file:
        file.write(f"{ip_address}\n")
        file.write(f"{timer_interval}\n")
        for index, state in checkbox_states.items():
            file.write(f"{index},{state}\n")

def load_config(config_file):
    # temp variables that will be passed to the functions
    ip_address = ""
    timer_interval = 100  # Default value
    checkboxes_states = {}
    
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                ip_address = lines[0].strip()
                timer_interval = int(lines[1].strip())
                checkboxes_states = {int(line.split(',')[0]): line.split(',')[1].strip() == 'True' for line in lines[2:]}

    return ip_address, timer_interval, checkboxes_states
