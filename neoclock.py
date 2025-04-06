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
# neoclock 1.0.0
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
        "neoclock_foreground_color": "",
        "neoclock_background_color": ""
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
        f.write("neoclock_foreground_color: \n")
        f.write("neoclock_background_color: \n")

def prompt_for_config(path):
    print("🚀 Welcome to neoclock! Let's create your config.")
    font = input("Choose font (default = standard): ") or "standard"
    fg = input("Text color (e.g., red, green, blank for default): ")
    bg = input("Background color (e.g., on_blue, on_yellow, blank for none): ")

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(f"neoclock_font: {font}\n")
        f.write(f"neoclock_foreground_color: {fg}\n")
        f.write(f"neoclock_background_color: {bg}\n")
    print("✅ Config saved. Launching neoclock...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_clock(color=None, font="standard", bgcolor=None):
    while True:
        clear_screen()
        current_time = datetime.now().strftime("%H:%M:%S")
        try:
            ascii_banner = pyfiglet.figlet_format(current_time, font=font)
        except pyfiglet.FontNotFound:
            print(f"⚠️ Font '{font}' not found. Using 'standard'.")
            ascii_banner = pyfiglet.figlet_format(current_time)

        if color:
            try:
                print(colored(ascii_banner, color=color, on_color=bgcolor))
            except KeyError:
                print(f"⚠️ Invalid color '{color}' or '{bgcolor}'. Falling back.")
                print(ascii_banner)
        else:
            print(ascii_banner)

        time.sleep(1)

def main():
    if is_root():
        print("❌ neoclock does not support running as root. Exiting.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="neoclock — your terminal timepiece in style.")
    parser.add_argument('-c', '--color', type=str, help="Text color (e.g., red, green, blue)")
    parser.add_argument('-f', '--font', type=str, help="Font for ASCII clock")
    parser.add_argument('--bg', type=str, help="Background color (e.g., on_blue)")
    parser.add_argument('--list-fonts', action='store_true', help="List available pyfiglet fonts")
    parser.add_argument('-i', '--info', action='store_true', help="Show neoclock version info")

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

    config = read_config(config_path)

    font = args.font or config["neoclock_font"]
    color = args.color or config["neoclock_foreground_color"]
    bgcolor = args.bg or config["neoclock_background_color"]

    display_clock(color=color, font=font, bgcolor=bgcolor if bgcolor else None)

if __name__ == "__main__":
    main()
