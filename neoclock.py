#                                            __                      __       
#                                           /  |                    /  |      
#    _______    ______    ______    _______ $$ |  ______    _______ $$ |   __ 
#   /       \  /      \  /      \  /       |$$ | /      \  /       |$$ |  /  |
#   $$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$$/ $$ |/$$$$$$  |/$$$$$$$/ $$ |_/$$/ 
#   $$ |  $$ |$$    $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |$$ |      $$   $$<  
#   $$ |  $$ |$$$$$$$$/ $$ \__$$ |$$ \_____ $$ |$$ \__$$ |$$ \_____ $$$$$$  \ 
#   $$ |  $$ |$$       |$$    $$/ $$       |$$ |$$    $$/ $$       |$$ | $$  |
#   $$/   $$/  $$$$$$$/  $$$$$$/   $$$$$$$/ $$/  $$$$$$/   $$$$$$$/ $$/   $$/ 
#                                                                             
#                                                                           
# neoclock 1.0.1
# Made by judeeey, published under the GNU GPL 3.0 license
# https://github.com/judeeey/neoclock                                          

import os
import sys
import time
import argparse
from datetime import datetime
import pyfiglet
from termcolor import colored
from pathlib import Path
import platform
import colorama

colorama.init()

VERSION = "1.0.1"
RELEASE_DATE = "06/04/2025"

COLOR_MAP = {
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "gray": (169, 169, 169),
}

def is_root():
    return os.geteuid() == 0 if hasattr(os, "geteuid") else os.name == 'nt' and 'SUDO_USER' in os.environ

def get_config_path():
    if platform.system() == "Windows":
        return Path(os.getenv('APPDATA')) / "neoclock" / "neoclock.conf"
    else:
        return Path.home() / ".config" / "neoclock" / "neoclock.conf"

def read_config(path):
    config = {
        "neoclock_font": "standard",
        "color1": "yellow",
        "color2": "orange",
    }
    if not path.exists():
        return None

    with open(path, "r") as f:
        for line in f:
            if line.strip() and ':' in line:
                key, value = line.strip().split(":", 1)
                config[key.strip()] = value.strip()
    return config

def create_default_config(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write("neoclock_font: standard\n")
        f.write("neoclock_color1: yellow\n")
        f.write("neoclock_color2: orange\n")

def prompt_for_config(path):
    print("🚀 Welcome to neoclock! Let's create your config.")
    font = input("Choose font (default = standard): ") or "standard"
    color1 = input("Start color for gradient (e.g., red): ") or "red"
    color2 = input("End color for gradient (e.g., blue): ") or "blue"

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(f"neoclock_font: {font}\n")
        f.write(f"neoclock_color1: {color1}\n")
        f.write(f"neoclock_color2: {color2}\n")
    print("✅ Config saved. Launching neoclock...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_gradient_colors(start_color, end_color, steps):
    start_rgb = COLOR_MAP.get(start_color.lower(), (0, 0, 0))
    end_rgb = COLOR_MAP.get(end_color.lower(), (255, 255, 255))

    gradient = []
    for step in range(steps):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * (step / (steps - 1)))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * (step / (steps - 1)))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * (step / (steps - 1)))
        gradient.append(f"\033[38;2;{r};{g};{b}m")
    
    return gradient

def apply_gradient_to_ascii(ascii_art, start_color, end_color):
    lines = ascii_art.split('\n')
    gradient = get_gradient_colors(start_color, end_color, len(lines))

    colored_lines = []
    for i, line in enumerate(lines):
        colored_line = f"{gradient[i]}{line}"
        colored_lines.append(colored_line)

    return "\n".join(colored_lines)

def display_clock(color1=None, color2=None, font="standard"):
    try:
        while True:
            clear_screen()
            current_time = datetime.now().strftime("%H : %M : %S")
            try:
                ascii_banner = pyfiglet.figlet_format(current_time, font=font)
            except pyfiglet.FontNotFound:
                print(f"⚠️ Font '{font}' not found. Using 'standard'.")
                ascii_banner = pyfiglet.figlet_format(current_time)

            if color1 and color2:
                gradient_ascii = apply_gradient_to_ascii(ascii_banner, color1, color2)
                print(gradient_ascii)
            else:
                print(ascii_banner)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹️  Exiting neoclock. Have a great day!")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="neoclock — your terminal timepiece in style.")
    parser.add_argument('-c1', '--color1', type=str, help="Start color of the gradient")
    parser.add_argument('-c2', '--color2', type=str, help="End color of the gradient")
    parser.add_argument('-f', '--font', type=str, help="Font for ASCII clock")
    parser.add_argument('--list-fonts', action='store_true', help="List available pyfiglet fonts")
    parser.add_argument('-i', '--info', action='store_true', help="Show neoclock version info")
    parser.add_argument('-rc', '--reset-config', action='store_true', help="Reset the configuration to default")

    args = parser.parse_args()

    if args.info:
        print(f"🕒 neoclock v{VERSION}\n📅 Released: {RELEASE_DATE}\n👤 Made by: judeeey\n🌐 GitHub: https://github.com/judeeey/neoclock")
        sys.exit(0)

    if args.list_fonts:
        print("Available fonts:\n")
        for f in pyfiglet.FigletFont.getFonts():
            print(f)
        sys.exit(0)

    config_path = get_config_path()

    if not config_path.exists():
        prompt_for_config(config_path)

    if args.reset_config:
        prompt_for_config(config_path)

    config = read_config(config_path)

    font = args.font or config["neoclock_font"]
    color1 = args.color1 or config["neoclock_color1"]
    color2 = args.color2 or config["neoclock_color2"]

    display_clock(color1=color1, color2=color2, font=font)

if __name__ == "__main__":
    main()
