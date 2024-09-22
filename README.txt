# ATEM Switcher Controller

A simple application to control an ATEM video switcher using a graphical interface. This tool allows you to connect to an ATEM switcher, set up program inputs, and automatically switch inputs based on a timer. It also provides tally monitoring to reset the timer when changes are detected.

## Features

- **Connect to ATEM Switcher:** Easily connect to an ATEM switcher using its IP address.
- **Automatic Input Switching:** Set up a timer to automatically switch program inputs.
- **Tally Monitoring:** Monitor tally changes to reset the timer automatically.
- **Cross-Platform:** Supports Windows, macOS, and Linux (executable needs to be built on the target platform).

## Installation

python3 -m venv atem_env
source venv/bin/activate
pip install -r requirements.txt

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
     ```bash
     pyinstaller --onefile --windowed switcher.py
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
      
