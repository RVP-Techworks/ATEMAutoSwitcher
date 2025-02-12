# ATEM Switcher Controller

A simple application to control an ATEM video switcher using a graphical interface. This tool allows you to connect to an ATEM switcher, set up program inputs, and automatically switch inputs based on a timer. It also provides tally monitoring to reset the timer when changes are detected.

## Features

- **Connect to ATEM Switcher:** Easily connect to an ATEM switcher using its IP address.
- **Automatic Input Switching:** Set up a timer to automatically switch program inputs.
- **Tally Monitoring:** Monitor tally changes to reset the timer automatically.
- **Cross-Platform:** Supports Windows, macOS, and Linux (executable needs to be built on the target platform).

## Installation

### On Linux Install tkinter
sudo apt-get install python3-tk
_Windows and mac should include this already with the default python install_

### Create and activate the virtual environment
python3 -m venv atem_env   # Linux/MacOS
# or
python -m venv atem_env    # Windows

#### Activate the virtual environment
source atem_env/bin/activate  # Linux/MacOS
# or
.\atem_env\Scripts\activate  # Windows

#### Install the dependencies
pip install -r requirements.txt

## Local Development
- When testing, you can run the "switcher.py" file to load the program
---------------------
### Windows

1. **Download the executable**: You can download the pre-built executable for Windows from the releases section.
2. **Run the executable**: Simply double-click the `.exe` file to run the application.

### macOS and Linux

For macOS and Linux, you'll need to create the executable on a machine running the respective operating system.

1. **Install Python and dependencies**:
   - Ensure you have Python 3 installed.
   - Install the required Python packages using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Build the executable**:
   - Install `PyInstaller` using:
     ```bash
     pip install pyinstaller
     ```
   - Generate the executable using:
   ## Windows
     ```bash
     pyinstaller --onefile --windowed --name ATEMAutoSwitcher --add-data "graphics/icon.png;graphics" --icon=graphics/icon.ico switcher.py
     ```
   ## Mac OSX
      First install pillow to convert the icon
      ```bash
      pip install pillow
      brew install tcl-tk
      ```
      Be sure to check line 25+ in GUI.py to make sure the Mac specific icon line is enabled, and the other one is commented out.

      run pyinstaller, pillow will automatically convert the file
      ```bash
      pyinstaller --onefile --windowed --name ATEMAutoSwitcher --add-data "graphics/icon.gif:graphics" --icon=graphics/icon.icns switcher.py
      ```
   ## Linux
   ```bash
   pyinstaller --onefile --windowed --name ATEMAutoSwitcher --add-data "graphics/icon.png:graphics" --icon=graphics/icon.png switcher.py
   ```


3. **Run the executable**:
   - For macOS, you'll find the `.app` file in the `dist` folder.
   - For Linux, you'll find the binary in the `dist` folder.

## Usage

1. **Launch the Application**:
   - Open the application by running the executable.
   
2. **Connect to ATEM Switcher**:
   - Enter the IP address of your ATEM switcher in the provided field.
   - Click "Connect" to establish a connection.

3. **Set Timer Interval**:
   - Adjust the timer interval (in seconds) for automatic input switching.

4. **Select Program Inputs**:
   - Check the inputs you want to include in the automatic switching.

5. **Start Monitoring**:
   - The application will monitor tally changes and reset the timer accordingly.

6. **Disconnect**:
   - To disconnect from the ATEM switcher, click the "Disconnect" button.

## Configuration

- **IP Address**: The IP address of the ATEM switcher is stored in `switcher_ip.txt` in the same directory as the executable.
- **Timer Interval**: The timer interval and selected inputs are also stored in `switcher_ip.txt`.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [PyATEMMax](https://github.com/teltek/PyATEMMax) for the Python library to interact with ATEM switchers.
- [PyInstaller](https://www.pyinstaller.org/) for creating standalone executables.

## Supported Devices

 - This should work with all ATEM switchers however, it has only been explicitly tested on:
      - ATEM Mini Pro
      - ATEM TV Studio HD
      - ATEM SDI ISO
      
