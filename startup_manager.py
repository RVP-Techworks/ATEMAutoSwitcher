import os
import platform
import sys
from pathlib import Path

def add_to_startup():
    system = platform.system()

    if system == "Windows":
        _add_to_startup_windows()
    elif system == "Darwin":  # macOS
        _add_to_startup_mac()
    elif system == "Linux":
        _add_to_startup_linux()

def remove_from_startup():
    system = platform.system()

    if system == "Windows":
        _remove_from_startup_windows()
    elif system == "Darwin":  # macOS
        _remove_from_startup_mac()
    elif system == "Linux":
        _remove_from_startup_linux()

def _add_to_startup_windows():
    startup_path = Path(os.getenv('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
    shortcut_path = startup_path / 'ATEMSwitcher.lnk'
    target = sys.executable
    start_in = Path(__file__).parent
    if not shortcut_path.exists():
        create_shortcut(target, start_in, shortcut_path)

def _remove_from_startup_windows():
    startup_path = Path(os.getenv('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
    shortcut_path = startup_path / 'ATEMSwitcher.lnk'
    if shortcut_path.exists():
        shortcut_path.unlink()

def _add_to_startup_mac():
    startup_item_path = Path.home() / 'Library' / 'LaunchAgents' / 'com.atemswitcher.plist'
    target = sys.executable
    start_in = Path(__file__).parent
    plist_content = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.atemswitcher</string>
        <key>ProgramArguments</key>
        <array>
            <string>{target}</string>
            <string>{start_in / Path(__file__).name}</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>WorkingDirectory</key>
        <string>{start_in}</string>
        <key>StandardOutPath</key>
        <string>{start_in / 'out.log'}</string>
        <key>StandardErrorPath</key>
        <string>{start_in / 'error.log'}</string>
    </dict>
    </plist>
    """
    with open(startup_item_path, 'w', encoding='utf-8') as f:
        f.write(plist_content)
    os.system(f"launchctl load {startup_item_path}")

def _remove_from_startup_mac():
    startup_item_path = Path.home() / 'Library' / 'LaunchAgents' / 'com.atemswitcher.plist'
    if startup_item_path.exists():
        os.system(f"launchctl unload {startup_item_path}")
        startup_item_path.unlink()

def _add_to_startup_linux():
    autostart_dir = Path.home() / '.config' / 'autostart'
    autostart_dir.mkdir(parents=True, exist_ok=True)
    desktop_entry = autostart_dir / 'ATEMSwitcher.desktop'
    target = sys.executable
    start_in = Path(__file__).parent
    desktop_entry_content = f"""
    [Desktop Entry]
    Type=Application
    Exec={target} {start_in / Path(__file__).name}
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name=ATEM Switcher
    Comment=Start ATEM Switcher on login
    """
    with open(desktop_entry, 'w', encoding='utf-8') as f:
        f.write(desktop_entry_content)

def _remove_from_startup_linux():
    desktop_entry = Path.home() / '.config' / 'autostart' / 'ATEMSwitcher.desktop'
    if desktop_entry.exists():
        desktop_entry.unlink()

def create_shortcut(target, start_in, shortcut_path):
    try:
        import win32com.client
        shell = win32com.client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = str(start_in)
        shortcut.save()
    except ImportError:
        print("win32com is required to create a shortcut on Windows. Please install pywin32.")

def is_open_at_startup():
    system = platform.system()

    if system == "Windows":
        startup_path = Path(os.getenv('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
        shortcut_path = startup_path / 'ATEMSwitcher.lnk'
        return shortcut_path.exists()
    elif system == "Darwin":  # macOS
        startup_item_path = Path.home() / 'Library' / 'LaunchAgents' / 'com.atemswitcher.plist'
        return startup_item_path.exists()
    elif system == "Linux":
        desktop_entry = Path.home() / '.config' / 'autostart' / 'ATEMSwitcher.desktop'
        return desktop_entry.exists()
    return False
