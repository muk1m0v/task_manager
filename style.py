from colorama import Fore, Style, init
import sys

init()

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
reset = Style.RESET_ALL
