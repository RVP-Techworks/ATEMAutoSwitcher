from PIL import Image

def convert_ico_to_icns(ico_path, icns_path):
    img = Image.open(ico_path)
    img.save(icns_path, format='ICNS')

if __name__ == "__main__":
    print("This script converts .ico files to .icns files for macOS.")
    ico_path = "graphics/icon.ico"  # Path to your .ico file
    icns_path = "graphics/icon.icns"  # Path to save the .icns file
    print("Converting .ico to .icns...")
    convert_ico_to_icns(ico_path, icns_path)