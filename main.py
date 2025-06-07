import subprocess
import pyautogui
import pygetwindow as gw
import time
import random
import nltk
from nltk.corpus import words

import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

nltk.download("words")

all_words = words.words()
random.shuffle(all_words)


try:
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input("How many searches need to perform? (10 by default): ").strip()
    search_count = int(user_input) if user_input else 10
except ValueError:
    print("Invalid input. Using default value of 10.")
    search_count = 10

# Launch Microsoft Edge
subprocess.Popen(["start", "msedge"], shell=True)
edge_window = None

print("Edge Browser start kar raha hu...")

def getRandomNames():
    path = resource_path("random_names.txt")
    with open(path, "r") as f:
        names = [line.strip() for line in f if line.strip()]
    name = random.choice(names)
    return name

def unique_word_generator():
    for word in all_words:
        yield word

for _ in range(20):
    windows = gw.getWindowsWithTitle("Edge")
    for win in windows:
        if "Edge" in win.title:
            edge_window = win
            break
    if edge_window:
        break
    time.sleep(0.5)

if edge_window:
    print("Edge is ready. Typing...")
    word_gen = unique_word_generator()
    edge_window.activate()
    for _ in range(search_count):
        pyautogui.hotkey("ctrl", "t")
        time.sleep(0.3)
        searchingFor = next(word_gen) + " " + getRandomNames()
        print(f"Searching for: {searchingFor}")
        pyautogui.write(searchingFor, interval=0.01)
        pyautogui.press("enter")
        time.sleep(1)
    print("Perfromed : ", search_count, "searches.")
    close_choice = input("Close Kar du saare opened Tabs? (y/n): ").strip().lower()
    if close_choice == "n" or close_choice == "no":
        print("Band Karlo Fir ek ek kar kar. Bye...")
        sys.exit()
    else:
        subprocess.call("taskkill /IM msedge.exe /F", shell=True)
else:
    print("Edge window not found.")
